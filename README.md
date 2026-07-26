# 🏥 Patient Management System (Flutter + Django REST Framework)

A full-stack application for tracking patient details, medical record numbers (MRN), room assignments, and personal contact details in a hospital setting. 

Built using **Django REST Framework** for the backend API and **Flutter** for a responsive, clean user interface.

---

## 🎯 Key Features

* **Patient Listing:** View patient details including Full Name, MRN, Age, Gender, Room Number, and Contact Info.
* **Add Patient:** Integrated form with validation to add new patient records.
* **REST API Integration:** Clean separation of UI and networking logic using a dedicated API Service layer.
* **CORS Enabled:** Fully configured to handle requests between Flutter Web and Django.

---

## 🛠️ Project Structure & Tech Stack

### 🔹 Backend (Django)
* **`models.py`**: Defines `PatientDetails` schema (Name, Age, Gender, Phone, Address, MRN, Room, Disease Description).
* **`serializers.py`**: `PatientDetailsSerializer` converting model instances to JSON.
* **`views.py`**: `PatientDetailsViewSet` providing CRUD endpoints using DRF `ModelViewSet`.
* **`urls.py`**: Standard REST routes registered using `DefaultRouter` under `/api/patients/`.

### 🔹 Frontend (Flutter)
* **`api_service.dart`**: Handles `GET` and `POST` network requests using the `http` package.
* **`main.dart`**: Renders the patient list screen and modal forms for adding patients.

---

## 🚀 How to Run

### 1. Backend Setup
```bash
# Navigate to backend directory
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django djangorestframework django-cors-headers

# Apply Migrations
python manage.py makemigrations
python manage.py migrate

# Run Server
python manage.py runserver
