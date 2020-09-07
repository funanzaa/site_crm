import django_filters
from .models import *


class HositalFilter(django_filters.FilterSet):

    class Meta:
        model = Hospitals
        fields = ['code', 'label', 'h_type']
