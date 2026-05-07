from flask import Flask, request
import time
from service import *
from db import init_db

app = Flask(__name__)

#--------request_id----


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
def delete_products(product_id):
    #data = request.get_json(silent=True) or {}
    #product_id = data.get('id', '')
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
    request_id = int(time.time() * 1000)

    return search_product_service(name, request_id)


# ------------------

if __name__ == '__main__':
  init_db()

  app.run(host="0.0.0.0", port=5000)
  

