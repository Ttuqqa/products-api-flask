
def success_response(message, data= None):
  return{
    'success':True,
    'message': message,
    'data':data,
    'erroe':None
  }
  
  
def error_response(message, error= None):
  return{
    'success': False,
    'message': message,
    'data': None,
    'error': error
  }