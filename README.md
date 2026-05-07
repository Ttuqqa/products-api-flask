# Products API (Flask + SQLite)

A simple RESTful API built with Flask and SQLite for managing products.

---

## 🚀 Features
- Add product
- Get all products
- Delete product by ID
- Update product by ID
- Search product by name
- Logging & error handling
- Input validation

---

## 🛠️ Tech Stack
- Python
- Flask
- SQLite
- Gunicorn

---

## 📌 API Endpoints

### Get all products
```http
GET /products
```

### Add product
```http
POST /products
```

### Delete product
```http
DELETE /products/<id>
```

### Update product
```http
PUT /products/<id>
```

### Search product
```http
GET /products/search?name=product_name
```

---

## 🌐 Live Demo

https://products-api-flask.onrender.com/

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

---

## 👩‍💻 Author

Toqa — Backend Developer (Python & Flask)

---