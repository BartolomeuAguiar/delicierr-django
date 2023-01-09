from django.urls import path

from . import views

app_name = 'clients'


urlpatterns = [
    path('', views.Create.as_view(), name='create'),
    path('clients/login/', views.Login.as_view(), name='login'),
]
