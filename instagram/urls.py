from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("post", views.PostViewSet) # 이 시점에 2개의 URL을 만들어준다.
# router.urls에 리스트 형태로 존재한다. url pattern list


# django urls에서 urlpatterns를 요구하기 때문에 반드시 있어야함.
urlpatterns = [
    path("", include(router.urls)),
]