from django.db import models

class todo(models.Model):
    title = models.CharField(max_length=200) 
    description = models.CharField(max_length=200) 
    completed = models.BooleanField(default=False) 
    deadline = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title