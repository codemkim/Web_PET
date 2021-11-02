from django.contrib import admin

# Register your models here.
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')

admin.site.register(Profile, ProfileAdmin)



