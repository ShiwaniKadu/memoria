# memoria
A simple Django-based web application for creating and managing journals with different types.
## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and authorization
- Create, read, update, and delete (CRUD) operations for journals
- Multiple journal types
- User-friendly interface

## Installation

### Prerequisites

- Python 3.6+
- Django 4.2
- Virtualenv (optional but recommended)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/journal-project.git
    cd journal-project
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

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

## Usage

1. Navigate to `http://127.0.0.1:8000/` in your web browser.
2. Log in with your superuser credentials.
3. Create new journal types.
4. Create, view, edit, and delete journals under different types.

## Folder Structure
