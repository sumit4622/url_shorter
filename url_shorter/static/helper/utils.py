from django.http import JsonResponse

def sucess_response( result: str, message :str):
    
    response = {
        "status": True,
        "result" : result,
        "message" : message
    }
    
    
    return JsonResponse(response, status = 200)

def error_response( result, message:str):
    
    response = {
        "status" : False,
        "result" : result,
        "message" : message
    }
    
    return JsonResponse(response, status =400)
    