from django.shortcuts import render, redirect
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your views here.
from FirstService.models import Profile,Result
from PIL import Image
import requests




# ssh -i flask_model.pem ubuntu@13.59.5.227

# python test.py



def home(request):

    return render(request, 'home.html')

def upload(request):

    return render(request, 'upload.html')

def select(request):

    return render(request, 'select.html')

def upload_create(request):

    form = Profile()
    form.image= request.FILES['image']

    form.save()
    profile = Profile.objects.get(id=form.id)

    return render(request, 'loading.html', {'profile':profile})

def learning(request, **kwargs):
    result_img = Result()
    profile = Profile.objects.get(id=kwargs['pk'])

    # 이미지 흑백 처리 간단 코드

    # output = BytesIO()
    #
    # temp_image = Image.open(profile.image_converted)
    # temp_image = temp_image.convert('L')
    #
    # temp_image.save(output, format='JPEG')
    # result_img.image = InMemoryUploadedFile(output,
    #                                         "ImageField",
    #                                         profile.image_converted.name,
    #                                         'image/jpeg',
    #                                         None,
    #                                         None)
    temp = profile.image_converted.name

    resp = requests.post("http://localhost:5000/predict",
                         files={"file": open('media/'+temp, 'rb')})
    save_path = "media/temp/result"+str(profile.id)+".jpg"
    photo = open(save_path, 'wb')
    photo.write(resp.content)
    photo.close()

    result_img.image = Image.open(save_path)
    result_img.save()

    return redirect('FirstService:result', pk=result_img.id)


def result(request, **kwargs):
    result = Result.objects.get(id=kwargs['pk'])
    return render(request, 'result.html', {'result':result})