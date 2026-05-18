import sqlite3
from db import *
from utils.logger import log
from utils.validation import *
from utils.error_handler import handle_errors
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from utils.secrets import SECRET_KEY
from utils.response import success_response, error_response


# ---------------- ADD PRODUCT ----------------
@handle_errors
def add_product_service(name, request_id):

    log('Add product request received', request_id)

    error = validate_product_name(name)
    if error:
        log(f'Validation failed for {name}: {error}', request_id, level='ERROR')
        return error_response(
            message='Validation failed',
            error=error
        ), 400

    add_product_to_db(name)

    log(f"Product added successfully: {name}", request_id)

    return success_response(
        message='Product created successfully',
        data={
            'name': name,
            'status': 'created'
        }
    ), 201


# ---------------- GET PRODUCTS ----------------
@handle_errors
def get_products_service(request_id):

    log("Get products request received", request_id)

    products = get_products_from_db()

    log(f"Fetched {len(products)} products", request_id)

    return success_response(
        message='Products retrieved successfully',
        data={
            'products': products,
            'count': len(products)
        }
    ), 200


# ---------------- DELETE PRODUCT ----------------
@handle_errors
def delete_product_service(product_id, request_id):

    log(f"Delete request received for id: {product_id}", request_id)

    if product_id is None:
        log("Validation failed: id is required", request_id=request_id, level="ERROR")
        return error_response(
            message='Validation failed',
            error='product_id is required'
        ), 400

    affected = delete_product_from_db(product_id)

    if affected == 0:
        log(f"Delete failed: id {product_id} not found", request_id=request_id, level="ERROR")
        return error_response(
            message='Delete failed',
            error=f'Product {product_id} not found'
        ), 404

    log(f"Product deleted successfully: {product_id}", request_id)

    return success_response(
        message='Product deleted successfully',
        data={
            'id': product_id,
            'status': 'deleted'
        }
    ), 200


# ---------------- UPDATE PRODUCT ----------------
@handle_errors
def update_product_service(product_id, name, request_id):

    log(f"Update request received for id: {product_id}", request_id)

    error = validate_product_name(name)
    if error:
        return error_response(
            message='Validation failed',
            error=error
        ), 400

    if not product_id:
        return error_response(
            message='Validation failed',
            error='product_id is required'
        ), 400

    affected = update_product_by_id_db(product_id, name)

    if affected == 0:
        return error_response(
            message='Update failed',
            error=f'Product {product_id} not found'
        ), 404

    return success_response(
        message='Product updated successfully',
        data={
            'id': product_id,
            'name': name,
            'status': 'updated'
        }
    ), 200


# ---------------- SEARCH PRODUCT ----------------
@handle_errors
def search_product_service(name, request_id):

    log(f"Search request received for: {name}", request_id)

    error = validate_product_name(name)
    if error:
        return error_response(
            message='Validation failed',
            error=error
        ), 400

    results = search_product_from_db(name)

    if not results:
        return error_response(
            message='Product not found',
            error=f'No product matching {name}'
        ), 404

    return success_response(
        message='Product found successfully',
        data={
            'name': name,
            'results': results,
            'count': len(results)
        }
    ), 200


# ---------------- REGISTER USER ----------------
@handle_errors
def register_user_service(username, password, request_id):

    log(f'register request received for {username}', request_id)

    error = validate_user(username, password)
    if error:
        return error_response(
            message='Validation failed',
            error=error
        ), 400

    hashed_password = generate_password_hash(password)

    add_user_to_db(username, hashed_password)

    return success_response(
        message='User registered successfully',
        data={
            'username': username,
            'status': 'registered'
        }
    ), 201


# ---------------- LOGIN USER ----------------
@handle_errors
def login_user_service(username, password, request_id):

    log(f"Login request received for {username}", request_id)

    error = validate_user(username, password)
    if error:
        return error_response(
            message='Validation failed',
            error=error
        ), 400

    user = get_user_by_username(username)

    if not user:
        return error_response(
            message='Authentication failed',
            error='Invalid username or password'
        ), 401

    stored_password = user[2]

    if not check_password_hash(stored_password, password):
        return error_response(
            message='Authentication failed',
            error='Invalid username or password'
        ), 401

    token = jwt.encode({
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    },
    SECRET_KEY,
    algorithm="HS256")

    return success_response(
        message='Login successful',
        data={
            'token': token,
            'status': 'authenticated'
        }
    ), 200