from django.urls import path , include
from . import views
urlpatterns = [

    path('students/',views.studentView),
    
    path('students/<int:pk>/',views.studentDetailView),
]
