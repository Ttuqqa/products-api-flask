from flask import Flask, request
from utils.auth import token_required
import time
from service import *
from db import *

app = Flask(__name__)


#-----------HOME-------------

@app.route('/')
def home():
    return {
        "success": True,
        "message": "Products API is running successfully"
    }

#--------REQUEST_ID---------


def generate_request_id():
    return str(time.time()*1000)

# ------------------ ADD ------------------

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json(silent=True) or {}
    name = data.get('name', '').strip().lower()
    request_id= generate_request_id()

    return add_product_service(name , request_id)

# ------------------ GET ------------------

  
  
@app.route('/products', methods=['GET'])
def get_products():
  request_id= generate_request_id()
  return  get_products_service(request_id)

# ------------------ DELETE ------------------


@app.route('/products/<int:product_id>', methods=['DELETE'])
@token_required
def delete_products(product_id):
    
    #data = request.get_json(silent=True) or {}
    #product_id = data.get('id', '')
    print("Current User:", request.current_user)
    request_id= generate_request_id()

    return delete_product_service(product_id, request_id)


# ------------- UPDATE BY ID --------------------

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product_by_id (product_id):
  data= request.get_json(silent=True) or {}
  #product_id= data.get('id',0)
  name= data.get('name','').strip().lower()
  request_id= generate_request_id()
  
  return update_product_service(product_id, name, request_id)

#------------------search--------------

@app.route('/products/search', methods=['GET'])
def search_product():
    #data = request.get_json(silent=True) or {}
    name = request.args.get('name', '').strip().lower()
    request_id = generate_request_id()

    return search_product_service(name, request_id)
  
#------------ADD_USER-------------
@app.route('/register', methods=['POST'])
def register():
  
  
  data= request.get_json(silent=True) or {}
  
  username= data.get('username','')
  password= data.get('password')
  request_id= generate_request_id()
  
  return register_user_service(username, password, request_id)
    
#-----------LOG IN-------------

@app.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    request_id = generate_request_id()

    return login_user_service(
        username,
        password,
        request_id
    )

# ------------------

if __name__ == '__main__':
  init_db()
  create_users_table()

  app.run(host="0.0.0.0", port=5000)
  

