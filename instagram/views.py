from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all() # Post.object.filter(is_public=True)
    serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all() # 데이터의 범위 지정, 로직마다 달라질 경우 get_queryset 사용가능
    serializer_class = PostSerializer
    # 이것만으로 post_list의 2개 분기, post_detail의 3개 분기를 지원한다. -> url이 2개 필요

    # request의 method에 맞는 함수를 호출하는 함수
    # ex) request.method가 GET이면 get()함수를 호출한다.
    def dispatch(self, request, *args, **kwargs):
        print("request.method:", request.method)
        print("request.body:", request.body) # logger를 사용하는 것을 권장
        print("request.POST:", request.POST)

        return super().dispatch(request, *args, **kwargs)



