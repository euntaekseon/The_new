# Generated by Django 2.2 on 2020-09-17 16:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcommunity', '0007_auto_20200918_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
