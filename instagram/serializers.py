from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post


# 모든 프로그래밍 언어의 통신에서 데이터는 반드시 바이트문자열로 표현되어야한다.
# 송신자: 객체를 문자열로 변환하여 데이터 전송 -> 직렬화
# 수신자: 수신한 문자열을 다시 객체로 변환하여 활용 -> 비직열화

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]

class PostSerializer(serializers.ModelSerializer):
    # username = serializers.ReadOnlyField(source="author.username")
    #
    # class Meta:
    #     model = Post
    #     fields = [
    #         "pk",
    #         "username",
    #         "message",
    #         "created_at",
    #         "updated_at"
    #     ]

    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = "__all__"

