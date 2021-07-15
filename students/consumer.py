from channels.generic.websocket import WebsocketConsumer
import json
from django.core import serializers
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
import channels.layers

from django.dispatch import receiver
from .models import Student
class WSConsumer (WebsocketConsumer):
    def connect(self): 
        async_to_sync(self.channel_layer.group_add)(
            'student_group',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        pass

    def events_alarm(self, event):
        self.send(text_data=json.dumps(  {'message':event['message']}       ))

    @staticmethod
    @receiver(post_save, sender=Student)
    def order_offer_observer(sender, instance, **kwargs):
        print('sadasd')
        layer = channels.layers.get_channel_layer()
        async_to_sync(layer.group_send)('student_group', {
            'type': 'events.alarm',
            'message': [{
                'fields': {'name':instance.name,'qualification':instance.qualification,'percentage':instance.percentage,}               
            }]
        })  

    def receive(self, text_data):
        data = serializers.serialize("json", Student.objects.all())
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': data
        }))