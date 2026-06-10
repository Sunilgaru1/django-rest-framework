import django_filters
from .models import Employee2

class Employee2Filter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact')

    class Meta:
        model = Employee2
        fields = ['designation']