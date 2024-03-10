# Event Planner

Event Planner is an app that allows you to organise an event and take care of all the necessary steps needed from an admin perspective.

## Description

This Django project is designed for creating events, schedules, surveys and many more.

## Prerequisites

- Python (3.7 or higher)
- PostgreSQL

## Setup Instructions

1. Create a Virtual Environment:

    ```python
    python -m venv venv
    ```

2. Activate Virtual Environment:

    ```python
    source env/bin/activate
    ```

3. Install Dependencies, create PostgresSQL Database and update database configuration by copying ".env.sample" file and filling the necessary information.
4. If any changes are made to the model run:

    ```python
    pip install -r requirements.txt
    python manage.py makemigrations
    ```

5. Run migration:

    ```python
    python manage.py migrate
    ```

6. Run development server:

    ```python
    python manage.py runserver
    ```

7. You can create a super user (if needed):

    ```python
    python manage.py createsuperuser
    ```
