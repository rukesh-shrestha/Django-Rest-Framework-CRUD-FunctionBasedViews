from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=200,blank=False,default="Task to do.")
    date = models.DateField(default=2022/1/24)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    




