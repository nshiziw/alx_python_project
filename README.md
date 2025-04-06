# Nestify API

Nestify is a web-based platform where users can browse houses available for sale or rent. The system provides functionality for property owners to list their properties and manage their listings, while admin users can oversee the platform, moderate users, and manage listings. Clients can search and view houses without authentication.

---

## Features

### Client Users

- Browse houses available for sale or rent without logging in.
- View details of a single house.

### Property Owners

- Register and log in.
- Create, update, and delete house listings.
- View and update their profile information.

### Admin Users

- View all property owners and their listings.
- View platform statistics (total houses, houses for rent, houses for sale, total users, total banned users).
- Delete property owners or house listings.
- Ban property owners for a period of time (in days).

---

## API Endpoints

### Authentication Endpoints

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and get JWT tokens
- `GET /api/auth/me/` - Get current user profile
- `PUT /api/auth/me/` - Update current user profile

### House Listing Endpoints

- `GET /api/houses/` - List all houses
- `POST /api/houses/` - Create a new house listing
- `GET /api/houses/<int:pk>/` - Get house details
- `PUT /api/houses/<int:pk>/` - Update house details
- `DELETE /api/houses/<int:pk>/` - Delete a house listing
- `GET /api/houses/user/<int:user_id>/` - Get houses listed by a specific user

### Admin Endpoints

- `GET /api/admin/statistics/` - Get platform statistics
- `GET /api/admin/users/` - List all users
- `GET /api/admin/users/<int:pk>/listings/` - Get user's listings
- `PUT /api/admin/users/<int:pk>/ban/` - Ban a user
- `DELETE /api/admin/users/<int:pk>/delete/` - Delete a user

---

## Admin Credentials

Default admin credentials for testing:

- Username: `nshizi`
- Email: `nshizi@gmail.com`
- Password: `Nshizi@123`

---

## Technologies Used

- **Backend**: Django (with Django REST Framework)
- **Database**: MySQL
- **Authentication**: JSON Web Tokens (JWT)
- **API Testing**: Postman, Thunder Client (VS Code Extension)

---

## Installation

### Prerequisites

- Python 3.x
- MySQL
- Pip (Python package manager)

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/nshiziw/nestify.git
   cd nestify
   ```
