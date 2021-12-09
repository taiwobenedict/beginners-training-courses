from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name="homepage" ),
    path('index/', views.index, name="index"),
    path('all-words/', views.all_words, name="all-words"),
    path('word/<slug:letter>/', views.letter_collection, name="letter-collection"),
    path('<meaning>/', views.meaning, name="meaning"),
   
]
