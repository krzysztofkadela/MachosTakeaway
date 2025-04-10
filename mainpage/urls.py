from django.urls import path
from .views import (
    index,
    add_comment,
    edit_comment,
    delete_comment,
    custom_login,
    custom_logout,
    user_comments,
)

urlpatterns = [
    path('', index, name='index'),
    path('add_comment/', add_comment, name='add_comment'),
    path('comments/edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path(
        'comments/delete/<int:comment_id>/',
        delete_comment, name='delete_comment'),
    path('user_comments/', user_comments, name='user_comments'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]
