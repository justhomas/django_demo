from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from students import views

urlpatterns = [
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
