## Description

Expense tracker application to manage expenses built with Django. 

## Installation

```bash
$ pip install -r requirements.txt
```

## Env setup

```bash
# Create .env file in project folder (expense_tracker) and add below VARIABLES
$ DB_NAME="expense_tracker"
$ DB_USER="username"
$ DB_PASSWORD="password"
$ DB_HOST="localhost"
$ DB_PORT="3306" # 5432
```

## Running the app

```bash
# Make migration
$ python manage.py makemigrations

# Migrate
$ python manage.py migrate

# Create super user
$ python manage.py createsuperuser

# Start server
$ python manage.py runserver
```

