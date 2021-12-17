from django.urls import path

from rest_framework import routers
from .views import PostViewSet,CommentViewSet

router = routers.SimpleRouter()
router.register('post', PostViewSet, basename='category')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [

]
urlpatterns += router.urls