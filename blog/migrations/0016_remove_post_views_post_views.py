# Generated by Django 4.2.2 on 2023-07-09 15:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0015_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(related_name='viewed_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
