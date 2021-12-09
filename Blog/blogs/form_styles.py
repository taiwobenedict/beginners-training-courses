from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('category','category')
choices_list = []
for item in choices:
    choices_list.append(item)
class PostForm(forms.ModelForm):
    """Form definition for Post."""

    class Meta:
        """Meta definition for Postform."""

        model = Post
        fields = ('title','author','body','category')
        #widgets is where we really handle the form styles
        widgets ={
           'title': forms.TextInput(attrs={'class':'form-control'}),
           'author': forms.Select(attrs={'class': 'form-control'}),
           'body': forms.Textarea(attrs={'class':'form-control'}),
           'category': forms.Select(choices=choices_list, attrs={'class':'form-control'})
           
        } 
