from django import forms
from .models import User 
from django.core.exceptions import ValidationError

class registration_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = [ 'phonenumber', 'email', 'password']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email exits.")
        return email
    
    def clean_phonenumber(self):
        phonenumber = self.cleaned_data.get('phonenumber')
        if User.objects.filter(phonenumber=phonenumber).exists():
            raise ValidationError("A phone number is already taken.")
        
        return phonenumber
      