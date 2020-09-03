from django.forms import ModelForm
from .models import *


class CaseForm(ModelForm):
    class Meta():
        model = Case
        fields = ('name','project', 'project_subgroup','resolution','service','hospitals','case_pic')
        # fields = '__all__'
