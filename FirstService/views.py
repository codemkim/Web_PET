from django.shortcuts import render, redirect

# Create your views here.
from FirstService.models import Profile, Result
from PIL import Image


def home(request):

    return render(request, 'home.html')

def upload(request):

    return render(request, 'upload.html')

def upload_create(request):
    form=Profile()
    try:
        form.image=request.FILES['image']

    except:
        pass
    form.save()
    profile = Profile.objects.get(id=form.id)
    return render(request, 'loading.html', {'profile':profile})

def learning(request, **kwargs):
    result_img = Result()
    profile = Profile.objects.get(id=kwargs['pk'])
    #이미지 흑백 처리 간단 코드
    # temp = Image.open(profile.image.path)
    # result_img.image = temp.convert('L')
    result_img.image = profile.image
    result_img.save()

    return redirect('FirstService:result', pk=result_img.id)


def result(request, **kwargs):
    result = Result.objects.get(id=kwargs['pk'])
    return render(request, 'result.html', {'result':result})