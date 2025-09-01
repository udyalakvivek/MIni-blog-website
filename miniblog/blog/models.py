from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from .utils import generate_summary

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
    # desc = models.TextField()
    desc = CKEditor5Field(config_name='extends')
    summry = models.TextField(blank=True , null= True)
    author = models.CharField(max_length= 100, default='Vivek..')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=70 , choices=CATEGORY_CHOICES, default='general' )
    
    # updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.desc:
            # save karte hi summary auto-generate ho jaye
            self.summry = generate_summary(self.desc, sentence_count=5)
            print(f"Summary generateeeeeeeeeeeeeeeeeeeeeeee in model ")
        super().save(*args, **kwargs)
        print('➡ miniblog/blog/models.py:38 hgd:')
        
    
    def __str__(self):
        return self.title
    
    
# #dashboard user profile 
# class user_profile(models.Model):
#     pic = models.ImageField(upload_to='images/')


# contact Form data 
class dasboard_page(models.Model):
    dpImage = models.ImageField(upload_to='images/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)