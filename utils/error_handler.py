import sqlite3
from utils.logger import log

def handle_errors(func):
  
  
  def wrapper (*args, **kwargs):
    
    request_id=kwargs.get('request_id')
    
    try:
      return func (*args, **kwargs)
    
    
    except sqlite3.IntegrityError:
      log( 'DB error: dublicate entry', request_id=request_id, level='ERROR')
      return {'success':False, 'error': 'resource already exists'},400
    
    
    except Exception as e :
      log (f'unexpected error {str(e)}', request_id= request_id, level= 'ERROR')
      return{'success':False, 'error': 'internal server error' },500
    
    
  return wrapper
      
    
    
    