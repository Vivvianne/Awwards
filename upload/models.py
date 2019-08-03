from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "images/",null = True)
    description = models.TextField()
    link = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    @classmethod
    def search_by_title(cls,search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post
    
    def __str__(self):
        return self.title
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        if img.height  > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save()
    
    
    
    
    
class Comments(models.Model):
    comment = models.CharField(max_length = 200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # profile = models.ForeignKey(Profile)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, default = "")

    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save()
    