from django.urls import path
from . import views
# 수정
# from .views import PostDeleteView
from post.views import post_list, post_detail, post_edit, post_delete, post_new, \
    answer, answer_list, post_list_staff, post_not_allowed, answer_detail, answer_edit, answer_delete, post_detail_staff, answer_list_staff

app_name = 'post'

urlpatterns = [
    path('post_list', post_list, name='post_list'),
    path('post_list_staff', post_list_staff, name='post_list_staff'),
    path('post/<pk>/', post_detail, name='post_detail'),
    path('new/', post_new, name='post_new'),
    #path('post/<int:pk>/new/', views.post_new, name='post_new'),
    path('post/<pk>/edit/', post_edit, name='post_edit'),
    path('post/<pk>/delete/', post_delete, name='post_delete'),
    # path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('answer_list', answer_list, name='answer_list'),
    path('answer_list_staff', answer_list_staff, name='answer_list_staff'),
    path('answer', answer, name='answer'),
    path('post_not_allowed', post_not_allowed, name='post_not_allowed'),
    path('staff/<pk>/', answer_detail, name='answer_detail'),
    path('staff/<pk>/edit/', answer_edit, name='answer_edit'),
    path('staff/<pk>/delete/', answer_delete, name='answer_delete'),
    # path('post_must_login', post_must_login, name='post_must_login'),
    path('post/<pk>/staff', post_detail_staff, name='post_detail_staff'),
]