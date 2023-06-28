from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=30)
    message = models.TextField(max_length=1000)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'Message from ' + self.name
    