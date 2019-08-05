from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListView,
    PostDetailView,
    # PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    # PostCommentView
)

urlpatterns = [
    path('', PostListView.as_view(), name='upload-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.post_save, name='post-create'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/', views.search_results, name='search_results'),
    path('comment/(<post_id>\d+)', views.add_comment, name='comment'),
    path('api/merch/', views.MerchList.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)