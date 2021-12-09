from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import AddCategoryForm, EditCategory
from blogs.models import Category,Post


class UserFormCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "users_authentication.html"
    success_url = reverse_lazy('users:login')

class LoginView(LoginView):
    template_name = 'login.html'
    
class LogoutView(LogoutView):
    template_name = 'logout.html'

def AddCategoryViews(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('http://127.0.0.1:8000/home')
    else:
        form = AddCategoryForm()
    return render(request, 'add_category.html', {'form':form})

