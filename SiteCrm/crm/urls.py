from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.dashboardPage , name = 'dashboard-page'),
    path('create_case/', views.createCase , name = 'create_case'),
    path('update_case/<str:pk>', views.updateCase , name = 'update_case'),
]
