from django import forms

from django import forms
from .models import Todo 

class todoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['Task', 'Date', 'Time']
        # widgets = {
        #     'date': forms.DateInput(attrs={'type': 'date'}),
        #     'time': forms.TimeInput(attrs={'type': 'time'}),
        # }
        # labels = {
        #     'task': 'Task',
        #     'date': 'Date',
        #     'time': 'Time',
        # }
        # help_texts = {                                
        #     'task': 'Enter the task description',
        #     'date': 'Enter the date for the task',   
        #     'time': 'Enter the time for the task', 
        # }
        
