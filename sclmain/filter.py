import django_filters
from .models import *
from django_filters import DateFilter, CharFilter


class StudentFilter(django_filters.FilterSet):
    stu_Id = CharFilter(max_length=100, lookup_expr="icontains")
    Name = CharFilter(max_length=100, lookup_expr="icontains")

    class Meta:
        model = Student
        fields = "__all__"
        
