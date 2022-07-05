from django.contrib import admin
from requests import post
from apirest.models import Post
# Register your models here.
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id_descuento', 'codigo_descuento']
