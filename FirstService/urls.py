from django.urls import path

from FirstService import views

app_name = 'FirstService'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('upload_create', views.upload_create, name='upload_create'),
    path('loading/<int:pk>', views.loading, name='loading'),
    path('result/', views.result, name='result'),
]