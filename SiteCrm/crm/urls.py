from django.urls import path
from .views import *


urlpatterns = [
    path('dashboard', DashboardPage , name = 'dashboard-page'),

]
