from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = [
            "pk",
            "author_username",
            "message",
            "created_at",
            "updated_at",
            "is_public",
            "ip"
        ]


# serializer 생성자에서 data=인자가 주어지면
# .is_valid()가 호출된 후
# .initial_data 필드에 접근가능
# .validated_data를 통해 유효성 검증에 토과한 값들이 .save()에 사용된다.
# .errors -> 유효성 검증 수행 후 오류내역
# .data -> 유효성 검증 후 갱신된 인스턴스에 대한 필드값 사전

# serializer 목적
# 1. 직렬화
# 2. 입력값에 대한 유효성 검증 후 디비 저장

# 직렬화의 경우
# 생성자의 instance 파라미터에 모델객체를 넘겨준다.

# 유효성 검사
# data 파라미터에 입력값을 넘겨준다.
# 필드정의 시 validators를 지정 또는 클래스 Meta.validators를 지정
# 필드레벨 -> validate_fieldname(self, value)
# 오브젝트레벨 -> validate(self, data)