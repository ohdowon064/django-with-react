from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all() # 데이터의 범위 지정, 로직마다 달라질 경우 get_queryset 사용가능
    serializer_class = PostSerializer

    # 이것만으로 post_list의 2개 분기, post_detail의 3개 분기를 지원한다. -> url이 2개 필요
    #

