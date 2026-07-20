# account/service/service.py
from ..models import User

def checkExistingData(**kwargs):
    phoneNumber = kwargs.get('phonenumber')
    emailAddress = kwargs.get('email')
    
    if isinstance(phoneNumber, list):
        if phoneNumber:
            phoneNumber = phoneNumber[0]
        else:
            phoneNumber = ''

    if isinstance(emailAddress, list):
        if emailAddress:
            emailAddress = emailAddress[0]
        else:
            emailAddress = ''
        
    if phoneNumber:
        phoneNumber = str(phoneNumber).strip()
    else:
        phoneNumber = ''

    if emailAddress:
        emailAddress = str(emailAddress).strip()
    else:
        emailAddress = ''
    
    if phoneNumber:
        if User.objects.filter(phonenumber=phoneNumber).exists():
            return True

    if emailAddress:
        if User.objects.filter(email=emailAddress).exists():
            return True
        
    return False