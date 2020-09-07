
import datetime
import pytz
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import HositalFilter

@login_required(login_url='login')
def dashboardPage(request):
    current_user = request.user.id
    case = Case.objects.filter(created_by=current_user).order_by('-id')[:10]

    context = {'check': 'data_search', "all_case": case}
    return render(request, 'cases/dashboard.html',context )


@login_required(login_url='login')
def createCase(request):
    form = CaseForm()
    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CaseForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            tz = pytz.timezone('Asia/Bangkok')
            obj.date_entered = datetime.datetime.now(tz=tz)
            try:
                obj.created_by = request.user
                upload_file = request.FILES['case_pic']
                fs = FileSystemStorage()
                name = fs.save(upload_file.name, upload_file)
                url = fs.url(name)
                obj.case_pic = url
            # print(upload_file.name)
            # print(upload_file.size)
                obj.save()
                return redirect('dashboard-page')
            except:
                obj.created_by = request.user
                form.save()
                return redirect('dashboard-page')
    context = {'form': form}
    return render(request, 'cases/case_form.html', context)

@login_required(login_url='login')
def updateCase(request, pk):
    case = Case.objects.get(id=pk)
    form = updateCaseForm(instance=case)

    if request.method == 'POST':
        form = updateCaseForm(request.POST, instance=case)
        if form.is_valid():
            obj = form.save(commit=False)
            tz = pytz.timezone('Asia/Bangkok')
            try:
                obj.created_by = request.user
                obj.update_at = datetime.datetime.now(tz=tz)
                upload_file = request.FILES['case_pic']
                fs = FileSystemStorage()
                name = fs.save(upload_file.name, upload_file)
                url = fs.url(name)
                obj.case_pic = url
            # print(upload_file.name)
            # print(upload_file.size)
                obj.save()
                return redirect('dashboard-page')
            except:
                obj.update_at = datetime.datetime.now(tz=tz)
                obj.created_by = request.user
                form.save()
                return redirect('dashboard-page')

    context = { 'form': form }
    return render(request, 'cases/case_form.html', context)

@login_required(login_url='login')
def deleteCase(request, pk):
    case = Case.objects.get(id=pk)
    if request.method == "POST":
        case.delete()
        return redirect('dashboard-page')
    context = {'case': case}
    return render(request, 'cases/delete.html', context)

@login_required(login_url='login')
def hospital(request):
    if request.method == 'POST':
        data = request.POST.copy()
        text_find = data.get('text_find')
        hospital = Hospitals.objects.filter(label__icontains=text_find) | Hospitals.objects.filter(code__icontains=text_find)
        context = {'hospital': hospital}
        return render(request, 'cases/hospital.html', context)
    return render(request, 'cases/hospital.html')


