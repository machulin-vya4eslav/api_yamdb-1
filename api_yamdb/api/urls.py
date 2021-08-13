from django.urls import include, path
from rest_framework import routers

from .views import (
    UserViewSet, CommentViewSet, ReviewViewSet,
    TitleViewSet, CategoryViewSet, GenreViewSet,
    code, signup, token
)


v1 = routers.DefaultRouter()
v1.register('users', UserViewSet, basename='users')
v1.register(r'titles', TitleViewSet, basename='titles')
v1.register(r'categories', CategoryViewSet, basename='categories')
v1.register(r'genres', GenreViewSet, basename='genres')
v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<rewiew_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
v1.register(r'titles/(?P<title_id>\d+)/reviews',
            ReviewViewSet, basename='reviews')

urlpatterns = [
    path('v1/', include(v1.urls)),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', token, name='login'),
    path('v1/auth/code/', code, name='code'),
]
