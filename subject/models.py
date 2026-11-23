from django.db import models

from accounts.models import User

# Create your models here.

class Course(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    trainer = models.ForeignKey(User,on_delete=models.CASCADE)

    fees = models.PositiveIntegerField()

    duration = models.CharField(max_length=200)

    languages = models.TextField()

    cover_picture = models.ImageField(upload_to="cover_pics",null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.trainer
    


