# Generated by Django 4.2.2 on 2023-06-28 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_profile_email_remove_profile_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
