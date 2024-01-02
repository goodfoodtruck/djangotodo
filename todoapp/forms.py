from django import forms

class AddTaskForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Ajouter une tâche'})
    )