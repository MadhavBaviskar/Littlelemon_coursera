# Little Lemon Restaurant API

Django + Django REST Framework project with MySQL configuration, menu CRUD, booking CRUD, Djoser registration/token authentication, HTML landing page and tests. The original course starter archive was not provided, so this is a self-contained reference implementation, not a modification of the course starter assets.

## Setup
1. Install Python 3.11, Pipenv and MySQL Server.
2. Create database and user:
```sql
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'littlelemon_user'@'localhost' IDENTIFIED BY 'ChooseAStrongPassword';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'littlelemon_user'@'localhost';
FLUSH PRIVILEGES;
```
3. `pipenv install` then `pipenv shell`. Copy `.env.example` to `.env` and configure credentials.
4. `python manage.py migrate` then `python manage.py runserver`.
5. Open http://127.0.0.1:8000/.

## Endpoints
- Menu CRUD: `/api/menu-items/` and `/api/menu-items/{id}/`
- Bookings CRUD: `/api/bookings/` and `/api/bookings/{id}/`
- Date filter: `/api/bookings/?date=YYYY-MM-DD`
- Registration: `POST /auth/users/`
- Token login/logout: `/auth/token/login/`, `/auth/token/logout/`
- Current user: `/auth/users/me/`
- Search/sort menu: `?search=salad`, `?ordering=price`

Menu reads are public; menu writes require staff/superuser or Manager group. Booking writes require authentication. Duplicate date/time is blocked by serializer validation and a database unique constraint.

## Tests
`python manage.py test restaurant`

## GitHub
`Readme.txt` contains peer-review paths. Run `git init`, `git add .`, `git commit -m "Build Little Lemon restaurant API"`, add your own GitHub remote, then `git push -u origin main`. Never commit `.env`.

The included migration and tests must be run in your configured environment. This archive has not been connected to your MySQL server or tested in your environment; verify the endpoints in Insomnia before submission.
