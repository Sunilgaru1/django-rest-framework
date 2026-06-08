from django.urls import path , include
from . import views
urlpatterns = [

    path('students/',views.studentView),

    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetail.as_view()),

    path('villagers/',views.Villagers.as_view()),

    path('villagers/<int:pk>/',views.VillagerDetail.as_view()),
]
