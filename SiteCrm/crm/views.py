from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def DashboardPage(request):
    return render(request, 'cases/dashboard.html')
