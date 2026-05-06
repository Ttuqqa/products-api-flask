import time


#---------LOG-----------
def log(message, request_id=None, level="INFO"):
    print(f'[{level}] [{time.strftime("%Y-%m-%d %H:%M:%S")}] [req={request_id}] {message}')
    
