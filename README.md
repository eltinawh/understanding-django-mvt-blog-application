# Understanding Django's MVT Architecture

This repository contains the code examples and hands-on projects from the article "Understanding Django's MVT Architecture: A Comprehensive Guide" ([Part 1 - Core Concepts](https://medium.com/@eltina_hutahaean/12836bb48dc6?source=friends_link&sk=6900e65041852cd051b235b097ba5b64) & [Part 2 - Hands-On Blog Application](https://medium.com/@eltina_hutahaean/8d504d152296?source=friends_link&sk=d93c8a1e22251fe725c85211d4d1533d)). It demonstrates the application of Django’s MVT(U) structure through a simple blogging application. The project includes features such as user authentication, blog post creation, editing, and deletion, all built using Django's MVT(U) architecture. Feel free to clone the repository to follow along with the tutorial and explore the code in detail.

## Requirement

Before you begin, make sure you have the following installed:
- Python 3.11 or higher
- pip (Python package installer)
- venv (Python virtual environment manager)
- git (version control system)

We will use Django version >=5.1.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/eltinawh/understanding-django-mvt-blog-application.git

# navigate to the project directory
cd blog
```

### 2. Set up a virtual environment
```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment (Linux/MacOS)
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations

Run the following commands to create the necessary database tables 
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

To access the Django admin panel, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up the admin credentials.

### 6. Run the development server

Start the development server to verify everything is working correctly.
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to see the application.

## Documentation

[Official Django Documentation](https://www.djangoproject.com/)