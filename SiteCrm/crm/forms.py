from django.forms import ModelForm
from django import forms
from .models import *


class CaseForm(ModelForm):
    hospitals = forms.ModelChoiceField(queryset=Hospitals.objects.order_by('label')) ## order in from
    class Meta():
        model = Case
        fields = ['name','project', 'project_subgroup','resolution','service','hospitals','case_pic','created_by']
        # fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['created_by'].initial = 1 # default created_by
            self.fields['name'].widget = forms.TextInput(attrs={"class":"form-control", 'required': False})
            self.fields['created_by'].widget = forms.HiddenInput()
            self.fields['name'].widget = forms.TextInput(attrs={"class":"form-control"})
            self.fields['project'].widget.attrs['class'] = 'form-control'
            self.fields['project_subgroup'].widget.attrs['class'] = 'form-control'
            self.fields['service'].widget.attrs['class'] = 'form-control'
            self.fields['hospitals'].widget.attrs['class'] = 'form-control'
            self.fields['resolution'].widget = forms.Textarea(attrs={"class":"form-control"})

class updateCaseForm(ModelForm):
    class Meta():
        model = Case
        fields = ['name','project', 'project_subgroup','resolution','service','hospitals','case_pic']
        # fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(updateCaseForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['name'].widget = forms.TextInput(attrs={"class":"form-control"})
            self.fields['resolution'].widget = forms.Textarea(attrs={"class":"form-control"})
