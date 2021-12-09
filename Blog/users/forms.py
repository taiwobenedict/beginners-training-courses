from django import forms
from blogs.models import Category,Post


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category',)
        widgets ={
            'category': forms.TextInput(attrs={'class':'form-control', 'col':40})
        }
         
class EditCategory(forms.ModelForm):
    class Meta:
        model = Post
        fields =('category',)
        widgets = {
            'category': forms.TextInput(attrs={'class':'form-control', 'col':40})
        }