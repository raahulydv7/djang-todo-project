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
        widgets = {
            'due_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['title', 'description', 'status']:
            self.fields[field].widget.attrs.update({'class': 'form-group'})
