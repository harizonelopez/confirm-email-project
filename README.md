# Django Email Authentication Project

This project is a basic Django application implementing a user authentication system with email confirmation. The project includes user registration, login, logout, and account activation via email.

## Features

- User registration with email confirmation
- User login and logout
- Home page with various views for authenticated and unauthenticated users
- Form validation using `django-crispy-forms` with Bootstrap 4 styling features

## Requirements

- Python 3.0x
- Django 3.0x
- `django-crispy-forms` for form handling and Bootstrap 4 integration

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/harizonelopez/confirm-email-project
    cd confirm-email project
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/scripts/activate  # On Mac use `venv\bin\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your browser and go to `http://127.0.0.1:8000/`
