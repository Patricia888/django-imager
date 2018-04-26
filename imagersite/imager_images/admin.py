from django.contrib import admin
from .models import Albums, Photo

# Register your models here.
admin.site.register((Albums, Photo))
