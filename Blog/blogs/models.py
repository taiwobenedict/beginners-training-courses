from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



class Category(models.Model):
    category = models.CharField(max_length=223, default= 'sport')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.category


class Post(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    body = models.TextField()
    category = models.CharField(max_length=255, default='sport')
    date_uploaded= models.DateTimeField(default= timezone.now)



    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title
        
    def get_absolute_url(self):     #this below snippet only work for a specific page with pk or id
        return reverse('blog:home',) #kwargs={'pk': self.pk})
    
