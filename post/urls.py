from django.urls import path
from . import views
# 수정
# from .views import PostDeleteView
from post.views import post_list, post_detail, post_edit, post_delete, post_new

app_name = 'post'

urlpatterns = [
    path('post_list', post_list, name='post_list'),
    path('post/<pk>/', post_detail, name='post_detail'),
    path('new/', post_new, name='post_new'),
    #path('post/<int:pk>/new/', views.post_new, name='post_new'),
    path('post/<pk>/edit/', post_edit, name='post_edit'),
    path('post/<pk>/delete/', post_delete, name='post_delete'),
    # path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
