#---------VALIDATE_NAME------


def validate_product_name(name):
  if not name:
    return 'input cannot be empty'
  if len(name)<3 :
    return 'input cannot be shorter than 3 letters'
  
  return None


#-----------------VALIDATE_USER-----------------

def validate_user(username, password):
  
  if not username or not password:
    return "user name and password are required"
  
  if len(password) < 6 :
    return "password must be atleast 6 characters"
  
  
  return None
