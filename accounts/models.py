from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.mail import send_mail

# Create your models here.


class User(AbstractUser):

    ROLE_CHOICES = (

        ('TRAINER', 'Trainer'),
        ('STUDENT', 'Student'),

    )

    phone = models.CharField(max_length=15, unique=True)

    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='STUDENT')

    def __str__(self):

        return self.username


class TrainerProfile(models.Model):

    trainer = models.OneToOneField(User,on_delete=models.CASCADE,related_name="trainer")

    specialization = models.CharField(max_length=100,null=True)

    skills = models.TextField(null=True)

    qualification = models.CharField(max_length=200,null=True)

    experience = models.CharField(max_length=200,null=True)

    profile_picture = models.ImageField(upload_to="cover_pics",null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.user.username


class StudentProfile(models.Model):

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")

    course = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passout_year = models.PositiveIntegerField(null=True)

    profile_picture = models.ImageField(upload_to="cover_pics",null=True)

    skills = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

def create_trainer_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "trainer":

        TrainerProfile.objects.create(trainer=instance)

post_save.connect(create_trainer_profile,User)

def create_student_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,User)

def send_invtation_mail(sender,instance,created,*args,**kwargs):

    if created and instance.role=="trainer" or instance.role=="student":

        send_mail(
            "Account creation confirmation",
            "You have successfully created your account in develop_lms",
            "thusharashaju21@gmail.com",
            ["soorajd683@gmail.com"],
        )

post_save.connect(send_invtation_mail,sender=User)
    