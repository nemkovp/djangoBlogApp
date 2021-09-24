from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('name','category','datas')

admin.site.register(Post, PostAdmin)

