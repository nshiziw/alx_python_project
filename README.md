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
