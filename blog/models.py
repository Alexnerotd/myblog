from django.db import models
from accounts.models import MyUser

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    pub_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        ordering = ['-pub_data']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
