from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# username = blog And password Fi

class blog_post(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('technology', 'Technology'),
        ('lifestyle', 'Lifestyle'),
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('books', 'Books'),
    ] 
    title = models.CharField(max_length= 150)
    desc = models.TextField()
    author = models.CharField(max_length= 100, default='Vivek..')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=70 , choices=CATEGORY_CHOICES, default='general' )
    
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
# #dashboard user profile 
# class user_profile(models.Model):
#     pic = models.ImageField(upload_to='images/')


# contact Form data 
class Contact_Form(models.Model):
    pass