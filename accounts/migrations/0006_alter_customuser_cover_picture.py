# Generated by Django 4.2.2 on 2023-07-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_cover_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cover_picture',
            field=models.ImageField(default='cover_pic/cover_pic.webp', upload_to='cover_pic/'),
        ),
    ]
