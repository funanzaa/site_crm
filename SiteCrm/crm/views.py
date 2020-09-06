
import datetime
import pytz
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
            obj.created_by = request.user
            upload_file = request.FILES['case_pic']
            fs = FileSystemStorage()
            name = fs.save(upload_file.name, upload_file)
            url = fs.url(name)
            obj.case_pic = url
            # print(url)
            # print(upload_file.name)
            # print(upload_file.size)
            obj.save()
            # form.save()
            return redirect('dashboard-page')
    context = { 'form': form }
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
            obj.update_at = datetime.datetime.now(tz=tz)
            upload_file = request.FILES['case_pic']
            fs = FileSystemStorage()
            name = fs.save(upload_file.name, upload_file)
            url = fs.url(name)
            obj.case_pic = url
            obj.save()
            # form.save()
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
