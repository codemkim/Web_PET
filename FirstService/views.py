from django.shortcuts import render, redirect

# Create your views here.
from FirstService.models import Profile


def home(request):

    return render(request, 'home.html')

def upload(request):

    return render(request, 'upload.html')

def upload_create(request):
    form=Profile()
    form.title=request.POST['title']
    try:
        form.image=request.FILES['image']
    except:
        pass
    form.save()
    return redirect('FirstService:loading', kwargs={'pk':form.id})


def loading(request, **kwargs):
    profile = Profile.objects.filter(id=kwargs['pk'])
    return render(request, 'loading.html', {'profile':profile})


def result(request):
    return render(request, 'result.html')