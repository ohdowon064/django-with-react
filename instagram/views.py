from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PublicPostListAPIView(generics.ListAPIView):
    # queryset = Post.objects.all() # Post.object.filter(is_public=True)
    queryset = Post.objects.filter(is_public=True)
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

# DRF의 기본 CBV인 APIView
# APIView 클래스 혹은 @api_view 데코레이터를 사용하는데 이들은 View에 여러 기본 속성을 부여한다.
# 1. renderer_classes
# 2. parser_classes
# 3. authentication_classes -> 유저식별
# 4. throttle_classes
# 5. permission_classes -> 식별된 유저에 대해서 리소스에 있어 접근레벨 정의
# 6. content_negotiation_class
# 7. metadata_class
# 8. versioning_class

# DRF 2가지 뷰 -> APIView, @api_view
# APIView =통합=> Generic =통합=> ViewSet
# APIView => Mixins => Generics => ViewSet
# Generic 까지는 하나의 URL만 처리
# ViewSet은 2개의 URL 처리 가능
# 직렬화/비직렬화, 인증체크, 사용량 제한체크, 권한 체크, API 버전체크를 자동으로 수행해준다.
# 커스텀가능

# @api_view()
# list로 어떤 메서드를 지원할 지 명시한다.
# ex) @api_view(["GET", "POST"])