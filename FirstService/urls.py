from django.urls import path

from FirstService import views

app_name = 'FirstService'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('select/', views.select, name='select'),
    path('upload/', views.upload, name='upload'),
    path('upload2/', views.upload2, name='upload2'),
    path('upload3/', views.upload3, name='upload3'),
    path('upload_create', views.upload_create, name='upload_create'),
    path('upload_create2', views.upload_create2, name='upload_create2'),
    path('upload_create3', views.upload_create3, name='upload_create3'),
    path('learning/<int:pk>', views.learning, name='learning'),
    path('result/<int:pk>', views.result, name='result'),
]