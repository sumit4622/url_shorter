from django import forms
from .models import User 
from django.core.exceptions import ValidationError

class registration_form(forms.ModelForm):
    confirm_password = forms.CharField(label='confirm_password', widget=forms.PasswordInput)
    
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
        
    def check_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise ValidationError("password must be same.")
        
        return password 
    
class login_form(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['email' ,'password']
        
    def check_email(self):
        if self.email != User.email:
            raise ValidationError("Account not created.")      