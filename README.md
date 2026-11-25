# 🎓 Learning Management System (LMS)

A REST API-based **Learning Management System (LMS)** developed using Django REST Framework. This project provides APIs for managing users, courses, trainers, students, and course modules.

## 🚀 Features

- 👤 Custom User Management
- 🎓 Student Registration
- 👨‍🏫 Trainer Registration
- 🔐 Token Authentication
- 📚 Course Management
- 📖 Course Module Management
- 👥 Role-Based Permissions
- 🖼️ Course Cover Image Upload
- 🔄 CRUD Operations
- 🗄️ Database Management

## 🛠️ Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- REST API
- Postman
- Git & GitHub

## 📂 Project Structure

```text
dev_lms/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── subject/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── units/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── dev_lms/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/thusharashaju21-droid/learning_lms.git
```

### 2. Navigate to the project directory

```bash
cd learning_lms
```

### 3. Create a virtual environment

```bash
python -m venv lms_env
```

### 4. Activate the virtual environment

**Windows:**

```bash
lms_env\Scripts\activate
```

### 5. Install dependencies

```bash
pip install django djangorestframework
```

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Server URL:

```text
http://127.0.0.1:8000/
```

## 🔑 Authentication

This project uses Token Authentication.

Include the token in request headers:

```http
Authorization: Token your_token_here
```

## 📡 API Testing

APIs are tested using **Postman** and VS Code REST Client.

## 👩‍💻 Developer

**Thushara V S**

Python Full Stack Developer | Django REST Framework

GitHub: [thusharashaju21-droid](https://github.com/thusharashaju21-droid)

---

⭐ Developed as a Python Django REST Framework project.
