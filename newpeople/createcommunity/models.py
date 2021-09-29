from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=100)
    goal = models.CharField(max_length=200)
    body = models.TextField()
    keyword = models.CharField(max_length=100)

    like_users = models.ManyToManyField('account.CustomUser', related_name='like_posts', blank=True)
    # detail 누르기 전 내용들만 띄우고, more 누르면 해당 포스트 detail화면에 띄우면 되지 않을까

    def __str__(self):
        return self.title
