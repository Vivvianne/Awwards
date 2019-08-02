from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "images/",null = True)
    description = models.TextField()
    link = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
    
    # img = image.open(self.image.path)
            
    # if img.height > 400 or img.width > 400:
    #     output_size =(400, 400)
    #     img.thumbnail(output_size)
    #     image.save(self.image.path)
    
    
class Comments(models.Model):
    comment = models.CharField(max_length = 200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # profile = models.ForeignKey(Profile)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, default = "")

    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save()
    