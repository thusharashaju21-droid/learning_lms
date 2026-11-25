from django.db import models

from subject.models import Course
from accounts.models import User

class Modules(models.Model):

    module_number = models.PositiveIntegerField(default=0)

    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course")

    title = models.CharField(max_length=300)

    description = models.TextField()

    duration = models.CharField(max_length=200)

    exam_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):

        if not self.pk:

            last_module_object = Modules.objects.filter(course=self.course).last()

            if last_module_object:

                self.module_number = last_module_object.module_number+1

            else:

                self.module_number = 1
        
            return super().save(*args,**kwargs)