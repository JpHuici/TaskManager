from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','task_manager','description','important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Write title'}),
            'task_manager': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Write name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Write description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input mb-2'}),
        }