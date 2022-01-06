from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all() # 데이터의 범위 지정, 로직마다 달라질 경우 get_queryset 사용가능
    serializer_class = PostSerializer

    @action(detail=False, methods=["GET"])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True) # self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True) # PostSerializer(qs, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=["PATCH"])
    def set_public(self, request, pk):
        instance = self.get_object() # GenericAPIView의 get_object() 사용
        instance.is_public = True
        instance.save(update_fields=["is_public"]) # is_public 필드만 업데이트
        serializer = self.get_serializer(instance)
        return Response(serializer.data)