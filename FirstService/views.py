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

    # 이미지 변환 코드

    temp = profile.image_converted.name

    resp = requests.post("http://3.16.37.62:5000/predict",
                         files={"file": open('media/'+temp, 'rb')})
    save_path = "media/temp/result"+str(profile.id)+".jpg"
    photo = open(save_path, 'wb')
    photo.write(resp.content)
    photo.close()

    image = Image.open(save_path)
    image = image.convert('RGB')
    image = image.resize((300, 300), Image.ANTIALIAS)
    output = BytesIO()
    image.save(output, format='JPEG', quality=85)
    output.seek(0)
    result_img.image = InMemoryUploadedFile(output, 'ImageField',
                                str(profile.id)+".jpg",
                                'image/jpeg',
                                sys.getsizeof(output), None)

    result_img.save()

    return redirect('FirstService:result', pk=result_img.id)


def result(request, **kwargs):
    result = Result.objects.get(id=kwargs['pk'])
    return render(request, 'result.html', {'result':result})