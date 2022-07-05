from django.contrib import admin
from .models import Categoria, Usuario, Vehiculo, PerfilUsuario, categoriaProducto, manBod, manProducto, Ventas

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(PerfilUsuario)
admin.site.register(categoriaProducto)
admin.site.register(manProducto)
admin.site.register(Usuario)
admin.site.register(manBod)
admin.site.register(Ventas)
