# Generated by Django 2.2 on 2020-09-17 16:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcommunity', '0004_auto_20200917_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
