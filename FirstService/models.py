from django.db import models
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
# Create your models here.


class Profile(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True)
    image_converted =models.ImageField(upload_to='images/', null=True)

    def save(self, *args, **kwargs):
        self.convert_image()
        self.image = None
        super(Profile, self).save(*args, **kwargs)

    def convert_image(self, *args, **kwargs):
        image_converted = convert_test(self.image)
        self.image_converted = InMemoryUploadedFile(file=image_converted,
                                                    field_name="ImageField",
                                                    name=self.image.name,
                                                    content_type='image/jpeg',
                                                    size=sys.getsizeof(image_converted),
                                                    charset=None)

def convert_test(img):
    img = Image.open(img)
    img = img.convert('RGB')
    img = img.resize((300, 300), Image.ANTIALIAS)
    return image_to_bytes(img)

def image_to_bytes(img):
    output = BytesIO()
    img.save(output, format='JPEG', quality=95)
    output.seek(0)
    return output


class Result(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='imagesResult/', null=True)

    def __str__(self):
        return self.title

