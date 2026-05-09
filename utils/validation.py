#---------VALIDATE_NAME------


def validate_product_name(name):
  if not name:
    return {'success': False, 'error':'input cannot be empty'},400
  if len(name)<3 :
    return {'success': False, 'error':'input cannot be shorter than 3 letters'},400
  
  return None


#-----------------VALIDATE_USER-----------------

def validate_user(username, password):
  
  if not username or not password:
    return{'success':False, 'error': 'username and password are required'},400
  
  if len(password) < 6 :
    return{'success': False, 'error':'password must be at least 6 characters'}, 400
  
  
  return None
