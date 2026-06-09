# In Serialization Data is Converted in JSON so we get url response in rest_framwork 
from rest_framework import serializers

from students.models import Student
from employees.models import Employee
from villagers.models import Villager
from hostellers.models import Hosteller
from employess2.models import Employee2

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

class VillagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Villager
        fields = "__all__"

class HostellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hosteller
        fields = "__all__"

class Employee2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Employee2
        fields = "__all__"