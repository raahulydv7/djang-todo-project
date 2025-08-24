 
# Django To-Do Application

A production-ready To-Do application built with **Django**, featuring:
- User authentication (Login, Register, Logout)
- Todo management with CRUD operations
- Categories (admin-defined)
- Status filters & search
- Pagination for todos
- Responsive design (ready for Bootstrap or custom CSS)

---

## Features

- **User Authentication**
  - Secure login and signup system
  - Session-based authentication
- **Todo Management**
  - Create, Update, Delete, and View todos
  - Filter by status and category
  - Search by title (case-insensitive)
  - Pagination for better performance
- **Admin Features**
  - Manage categories
  - View all users’ todos

---

## Project Structure

The project follows a **modular Django app structure**:
- `users/` – Handles authentication (login, signup, logout)
- `todo/` – Handles todo CRUD, categories, filters, and pagination
- `static/` – Contains CSS/JS/images
- `templates/` – Contains HTML templates for each app

---

## Requirements

- Python 3.10+
- Django 4.x
- (Optional) Virtualenv for isolated environment

---

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/django-todo-app.git
   cd django-todo-app

2. Create Virtual Environmen (Recommended)
    <pre>
        python -m venv venv
        source venv/bin/activate    # On macOS/Linux
        venv\Scripts\activate       # On Windows
    </pre>



3. Install Dependencies

    <pre>
        pip install -r requirements.txt
    </pre>


4. Set Up Database

    <pre>
        python manage.py migrate
    </pre>


5. Create Superuser

    <pre>
        python manage.py createsuperuser
    </pre>



6. Run Development Server

    <pre>
        python manage.py runserver
    </pre>
    


7. Open your browser:
    <pre>
        http://127.0.0.1:8000
    </pre>

Usage

<ul>
    <li>
    Register or login to manage your todos.
    </li>
        <li>
    Admin can create categories from the Django admin panel:
    <pre>
    http://127.0.0.1:8000/admin
    </pre>
    </li>
    
</ul>


Environment Variables (Optional)
You can use a .env file for production settings:

<pre>
    SECRET_KEY=your-secret-key
    DEBUG=False
    ALLOWED_HOSTS=127.0.0.1,localhost,yourdomain.com
</pre>



Production Deployment

1. Set DEBUG=False in settings.py

2. Configure ALLOWED_HOSTS

3. Collect static files:
    <pre>
    python manage.py collectstatic
    </pre>
    
4. Deploy using Gunicorn + Nginx (recommended)