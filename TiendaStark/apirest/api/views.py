from rest_framework.viewsets import ModelViewSet
from apirest.models import Post
from apirest.api.serializers import PostSerializer 

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()