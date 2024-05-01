from django.urls import path
from .views import *


urlpatterns = [
   path('', PostsList.as_view(), name='post'),
   path('add/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('comment/create/', CommentCreate.as_view(), name='comment_create'),
]