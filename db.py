import sqlite3

def get_connection():
  conn= sqlite3.connect('products.db',timeout=10)
  return conn
  
#---------------------init----------------------
def init_db():
  conn= get_connection()
  cursor= conn.cursor()
  
  cursor.execute('''
                 CREATE TABLE IF NOT EXISTS products (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT UNIQUE
                 )
                 ''')
  conn.commit()
  conn.close()
  
  
#------------------users_table----------------
  
def create_users_table():
  conn= get_connection()
  cursor= conn.cursor()
    
  cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT NOT NULL UNIQUE,
                     password TEXT NOT NULL
                   )
                   ''')
    
  conn.commit()
  conn.close()
  
  # ------------------ ADD ------------------

def add_product_to_db(name):
  
      conn= get_connection()
      cursor=conn.cursor()
      cursor.execute (' INSERT INTO products (name) VALUES (?)',
                      (name,))
      conn.commit()
      conn.close()
      
  
      
      
# ------------------ GET ------------------

def get_products_from_db():
  conn= get_connection()
  cursor= conn.cursor() 
  
  cursor.execute('SELECT id, name FROM products ORDER BY id')
  rows=cursor.fetchall()
  
  conn.close()
  
  return [{'id' : row[0], 'name': row[1]} for row in rows]
    
    
# ------------------ DELETE ------------------

def delete_product_from_db(product_id):
    
    conn = get_connection()
    cursor= conn.cursor()
    cursor.execute(' DELETE FROM products WHERE id=?',
                   (product_id,))
    
    conn.commit()
    affected= cursor.rowcount
    conn.close()
    
    return affected
    

# ------------- UPDATE BY ID --------------------

def update_product_by_id_db(product_id, name):
  conn= get_connection()
  cursor=conn.cursor()
  
  cursor.execute (
                 "UPDATE products SET name=? WHERE id=?" ,
                 (name, product_id) 
                 )
  
  conn.commit()
  affected= cursor.rowcount
  
  conn.close()
  
  return affected

#----------------search---------------

def search_product_from_db(name):
  
  conn= get_connection()
  cursor= conn.cursor()
  
  cursor.execute( "SELECT id, name FROM products WHERE name LIKE?", (f'%{name}%',) )
  
  rows= cursor.fetchall()
  conn.close()
  
  return[{'id': row[0], 'name': row[1]}  for row in rows]

#------------ADD_USER----------------

def add_user_to_db(username, password):
  conn= get_connection()
  cursor= conn.cursor()
  
  cursor.execute('INSERT INTO users (username,password) VALUES(?,?) ',
                 (username,password,))
  conn.commit()
  conn.close()
  
  
#-----------GET USER BY USERNAME--------

def get_user_by_username(username):
  
  conn= get_connection()
  cursor= conn.cursor()
  
  cursor.execute(' SELECT * FROM users WHERE username=?',
                 (username,))
  
  user= cursor.fetchone()
  conn.close()
  
  return user
  
                 
  

      

  