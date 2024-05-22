from django.contrib import admin
from .models import Image


# Register your models here.
@admin.register(Image)
class Image(admin.ModelAdmin):
    list_display = [ 'photo', 'date']