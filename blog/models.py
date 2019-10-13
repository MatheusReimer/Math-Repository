from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumb = models.ImageField(default='padrao.jpg',blank=True,width_field='width_field',height_field='height_field')
    height_field= models.IntegerField(default=0)
    width_field= models.IntegerField(default=0)
    clip = models.FileField(default='padrao.mp4', null=True)





    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})




