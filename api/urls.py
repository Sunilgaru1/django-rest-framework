from django.urls import path , include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees2',views.Employee2ViewSet,basename='employees2')
urlpatterns = [

    path('students/',views.studentView),

    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetail.as_view()),

    path('villagers/',views.Villagers.as_view()),
    path('villagers/<int:pk>/',views.VillagerDetail.as_view()),

    path('hostellers/',views.Hostellers.as_view()),
    path('hostellers/<int:pk>/',views.HostellerDetail.as_view()),

    path('',include(router.urls))

]
