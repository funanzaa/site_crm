from django.forms import ModelForm
from django import forms
from .models import *


class CaseForm(ModelForm):
    class Meta():
        model = Case
        fields = ['name','project', 'project_subgroup','resolution','service','hospitals','case_pic','created_by']
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['created_by'].initial = 1 # default created_by
            self.fields['created_by'].widget = forms.HiddenInput()
            self.fields['name'].widget = forms.TextInput(attrs={"class":"form-control"})
            # self.fields['project'].widget = forms.(attrs={"class":"form-control"})
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

# class CaseForm(forms.Form):
#     name = forms.CharField(label="Case Name", max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
#     projects = Project.objects.all()
#     projects_subgroup = Project_subgroup.objects.all()
#     services = Service.objects.all()
#     hospitals = Hospitals.objects.all().order_by('label')
#     project_list = []
#
#     for project in projects:
#         small_project = (project.id, project.name)
#         project_list.append(small_project)
#     project_subgroup_list = []
#     for project_subgroup in projects_subgroup:
#         small_project_subgroup = (project_subgroup.id, project_subgroup.name)
#         project_subgroup_list.append(small_project_subgroup)
#     service_list = []
#     for service in services:
#         small_service = (service.id, service.name)
#         service_list.append(small_service)
#     hospital_list = []
#     for hospital in hospitals:
#         small_hospital = (hospital.id, hospital.label)
#         hospital_list.append(small_hospital)
#
#     project = forms.ChoiceField( choices = project_list, widget=forms.Select(attrs={"class":"form-control"}))
#     project_subgroup = forms.ChoiceField(label="Project_Subgroup", choices = project_subgroup_list, widget=forms.Select(attrs={"class":"form-control"}))
#     created_by = forms.CharField(required=False, widget=forms.HiddenInput)
#     resolution = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     service = forms.ChoiceField(label="service", choices = service_list, widget=forms.Select(attrs={"class":"form-control"}))
#     hospital = forms.ChoiceField(choices = hospital_list, widget=forms.Select(attrs={"class":"form-control"}))
#     case_pic = forms.FileField(label="Case_pic",max_length=50,widget=forms.FileInput(attrs={"class":"custom-file-input"}),required=False)
