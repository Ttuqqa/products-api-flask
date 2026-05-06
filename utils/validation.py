#---------VALIDATE------


def validate_product_name(name):
  if not name:
    return {'success': False, 'error':'input cannot be empty'},400
  if len(name)<3 :
    return {'success': False, 'error':'input cannot be shorter than 3 letters'},400
  
  return None