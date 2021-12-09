from django.urls import path
from .views import UserFormCreateView, LoginView, LogoutView, UserFormCreateView, AddCategoryViews


app_name = 'users'
urlpatterns = [
    path('', UserFormCreateView.as_view(), name = 'user_registration'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(), name= 'logout'),
    path('registration/', UserFormCreateView.as_view(), name= 'registration'),
    path('addcategory/', AddCategoryViews, name= 'add_category'),
    
   


]
