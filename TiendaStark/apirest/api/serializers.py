from rest_framework.serializers import ModelSerializer
from apirest.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id_descuento', 'codigo_descuento']