# 🏥 Healthcare Backend (Django + DRF)

This project is a **Healthcare Management Backend** built using **Django Rest Framework (DRF)**.  
It includes user authentication (JWT), patient and doctor management, and mapping APIs, with Postman collection for testing.

---

## 🚀 Features
- JWT Authentication (Login & Signup)  
- Custom User Model  
- CRUD APIs for Patients & Doctors  
- Patient ↔ Doctor mapping  
- Pagination, Permissions, and CORS enabled  
- Postman collection for easy API testing  

---

## 🛠️ Setup Instructions

### 1️⃣ Clone Repository & Create Virtual Environment
```bash
git clone <your-repo-url>
cd what_bytes_assignment

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # (Windows PowerShell)
source .venv/bin/activate  # (Linux/Mac)
```

---

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup `.env` File  
Create a `.env` file in the project root:

```ini
DJANGO_SECRET_KEY=your-secret-key
DEBUG=1
ALLOWED_HOSTS=127.0.0.1,localhost

POSTGRES_DB=healthcare_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

---

### 4️⃣ Apply Migrations & Create Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

### 5️⃣ Run Server
```bash
python manage.py runserver
```

Server will be available at:  
👉 http://127.0.0.1:8000  

---

## 🔑 API Authentication

The project uses **JWT (JSON Web Token)** authentication.

1. Signup/Login to get a token.  
2. Copy the `access` token and set it in Postman:  
   ```
   Authorization → Bearer <your-token>
   ```

---

## 🧪 Postman Testing

1. Import the collection:  
   - File: **`WhatBytes_assign.json`** (in repo)  
   - Or import manually in Postman.

2. Import the environment file (optional):  
   - Update variables (`base_url`, `token`) for your system.

3. Test APIs:  
   - **Auth**: `/auth/signup/`, `/auth/login/`  
   - **Patients**: `/patients/`  
   - **Doctors**: `/doctors/`  
   - **Mappings**: `/mappings/`

---

## 📂 Project Structure
```
what_bytes_assignment/
│── apps/
│   ├── users/       # Custom User model & auth
│   ├── patients/    # Patient APIs
│   ├── doctors/     # Doctor APIs
│   └── mappings/    # Patient ↔ Doctor mapping
│── common/          # Shared utilities
│── config/
│   ├── settings/    # base.py, dev.py, prod.py
│   ├── urls.py      # Root URL routing
│── manage.py
│── .env             # Environment variables
│── WhatBytes_assign.json   # Postman collection
```

---

## ✅ Example Request Body

### Signup
```json
{
  "username": "piyush",
  "email": "piyush@example.com",
  "password": "StrongPass123"
}
```

### Patient Create
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "age": 30,
  "gender": "M"
}
```

### Doctor Create
```json
{
  "first_name": "Dr. Smith",
  "last_name": "Williams",
  "specialization": "Cardiology"
}
```

---

## 📌 Notes
- Always run migrations after modifying models.  
- Use `DEBUG=0` in production.  
- Keep `.env` and `SECRET_KEY` safe.  
