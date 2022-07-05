from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Vehiculo, Categoria, PerfilUsuario
from .views import administrar_productos

def poblar_bd(request):
    try:
        print("Verificar si existe usuario cliente.")
        if User.objects.filter(username="usuario_cliente").exists():
            print("Intentando eliminar usuario cliente.")
            User.objects.get(username="usuario_cliente").delete()
            print("Usuario cliente eliminado.")
        print("Iniciando creación de usuario cliente.")
        user = User.objects.create_user(username="usuario_cliente", password='Duoc@123')
        user.first_name = "Sebastian"
        user.last_name = "Arostica (Cliente)"
        user.email = "sebitaxuwu@duocuc.cl"
        user.is_superuser = False
        user.is_staff = False
        PerfilUsuario.objects.create(user=user, rut="11.111.111-K", direccion="Santiaguiño (Chile)")
        user.save()
        print("Usuario cliente fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario cliente: {err}")
    try:
        print("Verificar si existe usuario staff.")
        if User.objects.filter(username="usuario_staff").exists():
            print("Intentando eliminar usuario staff.")
            User.objects.get(username="usuario_staff").delete()
            print("Usuario staff eliminado.")
        print("Iniciando creación de usuario staff.")
        user = User.objects.create_user(username="usuario_staff", password='Duoc@123')
        user.first_name = "Bastian"
        user.last_name = "Espinosa (Staff)"
        user.email = "ba.espinosav@duocuc.cl"
        user.is_superuser = True
        user.is_staff = True
        PerfilUsuario.objects.create(user=user, rut="22.222.222-K", direccion="Santiago (Chile)")
        user.save()
        print("Usuario staff fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario staff: {err}")
    try:
        Vehiculo.objects.all().delete()
        print("Tabla productos fue truncada.")
        Categoria.objects.all().delete()
        print("Tabla Categoria fue truncada.")
        print("Iniciar poblamiento de tabla Categoria.")
        Categoria.objects.create(idCategoria=1, nombreCategoria="Perros")
        Categoria.objects.create(idCategoria=2, nombreCategoria="Gatos")
        Categoria.objects.create(idCategoria=3, nombreCategoria="Otros")
        print("Tabla Categoria fue poblada.")
    except Exception as err:
        print(f"Error al poblar tabla Categoria: {err}")
    try:
        print("Iniciar poblamiento de tabla productos.")
        Vehiculo.objects.create(patente="01",categoria=Categoria.objects.get(idCategoria=1),  modelo="Comida de perro",descripcion='Comida para perros de 13kg',descs='SI',desco='NO', imagen="images/alimentoP1.jpg", precio=12990 )
        Vehiculo.objects.create(patente="02",categoria=Categoria.objects.get(idCategoria=1),  modelo="Comida de perro",descripcion='Comida para perros de 5 kg ',descs='SI',desco='NO', imagen="images/alimentoP2.jpg", precio=9990)
        Vehiculo.objects.create(patente="03",categoria=Categoria.objects.get(idCategoria=2),  modelo="Comida de gato",descripcion='Comdida para gatos de 13KG',descs='SI',desco='NO', imagen="images/alimentoG1.png", precio=12990)
        Vehiculo.objects.create(patente="04",categoria=Categoria.objects.get(idCategoria=2),  modelo="Comida de gato",descripcion='Comida para gatos de 5kg',descs='SI',desco='NO', imagen="images/alimentoG2.png", precio=9990)
        Vehiculo.objects.create(patente="05",categoria=Categoria.objects.get(idCategoria=3),  modelo="Comida de gato",descripcion='Correa para mascota',descs='SI',desco='NO', imagen="images/product-3.png", precio=4990)
        
        print("Tabla Productos fue poblada.")
    except Exception as err:
        print(f"Error al poblar productos: {err}")
    return redirect(administrar_productos, action='ins', id = '-1')