from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CommentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'posts', PostViewSet)

# Nested router for comments under posts
comments_router = DefaultRouter()
comments_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    
    path('', include(router.urls)),
    path('posts/<int:post_pk>/', include(comments_router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]




