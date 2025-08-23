from django import forms
from .models import Todo,Category

class TodoForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class':'form-control'})

    )
    class Meta:
        model = Todo
        fields = ['title', 'description', 'category', 'status', 'due_date']