# Local Artwork Showcase

## Project Overview
The **Local Artwork Showcase** is a web platform built with Django, Django REST Framework, and PostgreSQL. It allows local artists to share their artworks with the community by uploading images, descriptions, and other relevant details. The platform uses JWT-based authentication to ensure secure access.

## Features
- **User Authentication**: Secure login using JWT tokens (access and refresh tokens).
- **User Registration**: Artists can sign up to showcase their work.
- **Artist Profiles**: Artists can manage their profiles and view their uploaded artworks.
- **Artwork Management**: CRUD operations for artworks, accessible only to authenticated users.
- **Role-Based Access**: Artists can edit or delete only their own artworks.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)

## Installation

1. **Clone the repository:**
```bash
git clone <repository_url>
cd Local-Artwork-Showcase
```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure PostgreSQL:**
Update the `DATABASES` settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<your_db_name>',
        'USER': '<your_db_user>',
        'PASSWORD': '<your_db_password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. **Apply migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser (optional):**
```bash
python manage.py createsuperuser
```

7. **Run the server:**
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- **POST** `/api/account/register/` - Register a new user
- **POST** `/api/account/login/` - Log in and receive access/refresh tokens
- **POST** `/api/account/profile/` - User's Profile

### Artist Profiles
- **GET** `/api/art/artists/` - List all artist profiles
- **GET** `/api/art/artists/<id>/` - Retrieve a single artist profile
- **PUT** `/api/art/artists/<id>/` - Update artist profile (only by the owner)

### Artworks
- **GET** `/api/art/artworks/` - List all artworks
- **POST** `/api/art/artworks/` - Create a new artwork (authenticated users only)
- **GET** `/api/art/artworks/<id>/` - Retrieve details of an artwork
- **PUT** `/api/art/artworks/<id>/` - Update an artwork (only by the owner)
- **DELETE** `/api/art/artworks/<id>/` - Delete an artwork (only by the owner)

## JWT Authentication
The application uses JWT tokens for authentication. After logging in, include the token in the `Authorization` header:
```http
Authorization: Bearer <access_token>
```

## Security Best Practices
- Always store database credentials securely (e.g., using environment variables).
- Use strong passwords and rotate them periodically.
- Keep dependencies updated regularly.



