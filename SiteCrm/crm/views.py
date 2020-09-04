from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
# Create your views here.


def DashboardPage(request):
    current_user = request.user.id
    case = Case.objects.filter(created_by=current_user).order_by('-date_entered')[:10]
    context = {'check': 'data_search', "all_case": case}
    return render(request, 'cases/dashboard.html',context )

def CreateCase(request):
    # user = request.user
    form = CaseForm()
    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = CaseForm(request.POST)
        if form.is_valid():
            # name = request.POST.get("name")
            # project = request.POST.get("project")
            # project_subgroup = request.POST.get("project_subgroup")
            # created_by = request.POST.get("created_by")
            # resolution = request.POST.get("resolution")
            # service = request.POST.get("service")
            # hospitals = request.POST.get("hospitals")
            # print('Printing POST:')
            # case_pic = request.POST.get("service")
            print('Printing POST: ', request.POST)
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            # form.save()
            return redirect('dashboard-page')

    context = { 'form': form }
    return render(request, 'cases/case_form.html', context)
