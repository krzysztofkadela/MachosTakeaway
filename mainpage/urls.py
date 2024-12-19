from django.urls import path
from .views import index, add_comment, edit_comment, delete_comment  # Importing views
from .views import custom_login, custom_logout, user_comments #importing views line 2

urlpatterns = [
    path('', index, name='index'),  # Map the root URL to the index view
    path('add_comment/', add_comment, name='add_comment'),# add comment
    path('comments/edit/<int:comment_id>/', edit_comment, name='edit_comment'),# edit comment
    path('comments/delete/<int:comment_id>/', delete_comment, name='delete_comment'),# delete comment
    path('user_comments/', user_comments, name='user_comments'),# user comment
    path('login/', custom_login, name='login'),  # login path
    path('logout/', custom_logout, name='logout'),
]