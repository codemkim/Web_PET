from django.urls import path

from FirstService import views

app_name = 'FirstService'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('upload_create', views.upload_create, name='upload_create'),
    path('learning/<int:pk>', views.learning, name='learning'),
    path('result/<int:pk>', views.result, name='result'),
]