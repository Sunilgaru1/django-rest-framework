from django.shortcuts import render
from django.http import JsonResponse

from students.models import Student
from .serializers import StudentSerializer ,EmployeeSerializer,VillagerSerializer,HostellerSerializer,Employee2Serializer

from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

from rest_framework.views import APIView

from employees.models import Employee

from django.http import Http404

from villagers.models import Villager
from rest_framework import mixins

from hostellers.models import Hosteller
from rest_framework import generics

from employess2.models import Employee2
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer,CommentSerializer

from .paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend

from employess2.filters import Employee2Filter
# Create your views here.

# MANUAL SERIALIZER USING LIST FUNCTION



# FUNCTION BASED VIEWS

@api_view(['GET','POST'])
def studentView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer  = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CLASS BASED VIEWS

class Employees(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class EmployeeDetail(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee,data=request.data)

    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# MIXINS

class Villagers(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Villager.objects.all()
    serializer_class =VillagerSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class VillagerDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Villager.objects.all()
    serializer_class =VillagerSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)
    
# GENERICS

class Hostellers(generics.ListCreateAPIView):
    queryset = Hosteller.objects.all()
    serializer_class = HostellerSerializer

class HostellerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hosteller.objects.all()
    serializer_class = HostellerSerializer
    lookup_field = 'pk'


'VIEWSETS'

# class Employee2ViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Employee2.objects.all()
#         serializer = Employee2Serializer(queryset,many = True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def create(self,request):
#         serializer = Employee2Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
        
#     def retrieve(self,request,pk=None):
#         employee2 = get_object_or_404(Employee2,pk=pk)
#         serializer = Employee2Serializer(employee2)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def update(self,request,pk=None):
#         employee2 = get_object_or_404(Employee2,pk=pk)
#         serializer = Employee2Serializer(employee2,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,request,pk=None):
#         employee = get_object_or_404(Employee2,pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


'MODEL_VIEWSET'

# PAGINATION 
# FILTERRING
class Employee2ViewSet(viewsets.ModelViewSet):
    queryset = Employee2.objects.all()
    serializer_class = Employee2Serializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['designation']


# NESTED VIEWS
class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
