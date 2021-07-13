from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name','qualification','percentage')

    def validate_percentage(self,value):
        if value >100:
            raise serializers.ValidationError('This field must be less than or equal to 100')
        if value <0:
            raise serializers.ValidationError('This field must be greater than or equal to 0')
        return value
