from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    ROLE_CHOICES = (

        ('ADMIN', 'Admin'),
        ('TRAINER', 'Trainer'),
        ('STUDENT', 'Student'),

    )

    phone = models.CharField(max_length=15, unique=True)

    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='STUDENT')

    def __str__(self):

        return self.username


class TrainerProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='trainer_profile')

    qualification = models.CharField(max_length=200)

    experience = models.IntegerField()

    specialization = models.CharField(max_length=200)

    bio = models.TextField(null=True)

    profile_picture = models.ImageField(upload_to='trainer_profiles',null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user.username


class StudentProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_profile')

    qualification = models.CharField(max_length=200)

    start_year = models.IntegerField(null=True)

    passout_year = models.IntegerField(null=True)

    skills = models.TextField(null=True)

    linkedin_url = models.URLField(null=True)

    github_url = models.URLField(null=True)

    date_of_birth = models.DateField(null=True)

    profile_picture = models.ImageField(upload_to='student_profiles',null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username