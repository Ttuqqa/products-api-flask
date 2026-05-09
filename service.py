import sqlite3
from db import *
from utils.logger import log
from utils.validation import *
from utils.error_handler import handle_errors
from werkzeug.security import generate_password_hash


#---------ADD-----------
@handle_errors
def add_product_service(name, request_id):
  
    log('Add product request received', request_id)
  
    error = validate_product_name(name)
    if error:
      log(f'Validation failed for {name}: {error}', request_id, level= 'ERROR')
      return error
      
      
    
    log(f"Adding product to DB: {name}", request_id)
    add_product_to_db(name)

    log(f"Product added successfully: {name}", request_id)
    return {'success': True, 'data': f'{name} added successfully'}, 201

  

#---------------GET-------------
@handle_errors
def get_products_service(request_id):

    log("Get products request received", request_id)

    
    log("Fetching products from DB", request_id)

    products = get_products_from_db()

    log(f"Fetched {len(products)} products", request_id)

    return {'success': True,'data': products}, 200



#--------DELETE-------
@handle_errors
def delete_product_service(product_id, request_id):

    log(f"Delete request received for id: {product_id}", request_id)

    if product_id is None:
        log("Validation failed: id is required", request_id=request_id, level="ERROR")
        return {'success': False, 'error': 'id is required'}, 400

    affected = delete_product_from_db(product_id)

    if affected == 0:
        log(f"Delete failed: id {product_id} not found", request_id=request_id, level="ERROR")
        return {'success': False, 'error': f'{product_id} not found'}, 404

    log(f"Product deleted successfully: {product_id}", request_id)
    return {'success': True, 'data': f'product {product_id} deleted successfully'}, 200
      
      
# ------------- UPDATE BY ID --------------------
@handle_errors
def update_product_service(product_id, name, request_id):

    log(f"Update request received for id: {product_id}", request_id)
    
    error= validate_product_name(name)
    if error :
      log(f'Validation failed: {error} ({name})', request_id=request_id, level='ERROR')
      return error

    if not product_id:
        log("Validation failed: id is required",
            request_id=request_id, level="ERROR")
        return {'success': False, 'error': 'id is required'}, 400

    
    log(f"Updating product {product_id} to: {name}", request_id)

    affected = update_product_by_id_db(product_id, name)

    if affected == 0:
            log(f"Update failed: id {product_id} not found",
                request_id=request_id, level="ERROR")
            return {'success': False,'error': f'product with id {product_id} not found'
                    }, 404

    log(f"Product updated successfully: {product_id}", request_id)
    return {'success': True,'data': f'product {product_id} updated successfully to {name}'}, 200


      
#----------------search---------------

@handle_errors
def search_product_service(name, request_id):

    log(f"Search request received for: {name}", request_id)

    error = validate_product_name(name)
    if error:
        log(f'Validation failed for input: {name}', request_id, level='ERROR')
        return error

    results = search_product_from_db(name)

    if not results:
        log(f'{name} not found', request_id, level='ERROR')
        return {'success': False,'error': f'{name} not found'}, 404

    log(f"Product found: {name}", request_id)

    return {"success": True, "data": results, 'message':f'{name} found'}, 200
  
  
#---------------REGISTER_USER--------------
@handle_errors
def register_user_service(username, password, request_id):
  
  log(f'register request recieved for {username}', request_id)
  
  error= validate_user(username, password)
  if error:
    log(f'Validation failed {error}', request_id, level='ERROR')
    return error
  
  hashed_password= generate_password_hash(password)
  
  add_user_to_db(username, hashed_password)
  
  log(f'User registered successfully {username}', request_id)
  return{'sucsess': True, 'data':f'user {username} registered successfully'}, 201