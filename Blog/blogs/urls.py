from django.urls import path
from .views import *


app_name = 'blog'
urlpatterns = [
    path('home/', HomeListView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('add_post/', AddPostCreateView.as_view(), name= 'add_post'),
    path('edit_post/<int:pk>/', EditPostUpdateView.as_view(), name= 'edit_post'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    path('category/<str:cate>/', CategoryView, name = 'category'),
]