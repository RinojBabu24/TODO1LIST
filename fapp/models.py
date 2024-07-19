from django.db import models

class Todo(models.Model):
    Task = models.CharField(max_length=100, help_text="Enter the task")
    Date = models.DateField(help_text="Enter the date of the task")
    Time = models.TimeField(help_text="Enter the time of the task")

    def __str__(self):
        return self.Task

   

