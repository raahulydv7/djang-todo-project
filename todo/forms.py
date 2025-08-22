from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class CusUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ['username','email','role','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['username','email','role','password1','password2']:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs.update({'class': 'form-group'})