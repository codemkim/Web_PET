from django.urls import path

from FirstService import views

app_name='first_service'

urlpatterns = [
    path('home/', views.home, name='home')
]