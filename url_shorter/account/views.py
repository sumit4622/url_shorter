from django.shortcuts import render, redirect
# from .forms import registration_form
from django.contrib.auth.hashers import make_password
from .models import User
from django.http import HttpResponse, JsonResponse
# Inside account/views.py
from static.helper.utils import sucess_response, error_response
from .service.service import checkExistingData
# from templates/account/forgetpassword.html

# Create your views here.


def login (request):
    if request.method == 'POST':
        pass
        
    return render(request,'account/sign-in.html')


def register(request):
    if request.method == 'POST':
        postData = request.POST
        
        try:
            duplicateCheck = checkExistingData(**postData)
            print(duplicateCheck)
            
            if duplicateCheck == True: 
                return error_response("ERROR", "Account already exists.")
            else:
                
                first_name = postData.get('firstname', '').strip()
                last_name = postData.get('lastname', '').strip()
                phone_number = postData.get('phonenumber', '').strip()
                email = postData.get('email', '').strip()
                password = postData.get('password')
                confirm_password = postData.get('confirm_password')
                
                fullname = f"{first_name} {last_name}".strip()
                
                if password == confirm_password:
                    try:
                        user = User(
                            username = fullname,
                            phonenumber = phone_number,
                            email = email,
                            password = make_password(password)
                        )
                        user.save()
                        return sucess_response('ok', "User created successfully.")
                        
                    except Exception as e:
                        return error_response(False, "User account couldn't be created.")
                else:
                    return error_response("ERROR", "Passwords didn't match.")
                                
        except Exception as e:
            return error_response("ERROR", f"An unexpected error occurred: {str(e)}")
            
    else:
        return render(request, 'account/sign-up.html')    
def forgetpassword(request):
    return render(request,'account/forgetpassword.html')
    
    # print("this is some thing.")
    
def verify_otp(request):
    # from = request.post()
    # print(from)
    pass

