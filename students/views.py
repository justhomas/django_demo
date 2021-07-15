from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework import permissions 

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
    permission_classes=[permissions.AllowAny]
    
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes=[permissions.AllowAny]