from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.


def DashboardPage(request):
    current_user = request.user.id
    case = Case.objects.filter(created_by=current_user).order_by('-date_entered')[:10]
    context = {'check': 'data_search', "all_case": case}
    return render(request, 'cases/dashboard.html',context )

# def case(request):
#     current_user = request.user.id
#     print(current_user)
