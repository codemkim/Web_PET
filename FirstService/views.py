from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'home.html')

def upload(request):

    return render(request, 'upload.html')

def loading(request):

    return render(request, 'loading.html')


def result(request):
    return render(request, 'result.html')