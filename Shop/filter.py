import django_filters
from .models import *
from django_filters import CharFilter,RangeFilter
class productFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['demand','brand','category','name']