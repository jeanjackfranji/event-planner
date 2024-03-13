# Event Planner

Event Planner is an app that allows you to organise an event and take care of all the necessary steps needed from an admin perspective.
Wiki Documentation is available for [more details]<https://github.com/jeanjackfranji/event-planner/wiki>.

## Description

This Django project is designed for creating events, schedules, surveys and many more.

## Prerequisites

- Python (3.7 or higher)
- PostgreSQL

## Setup Instructions

1. Create a Virtual Environment:

    ```python
    python -m venv env
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

8. Use pip freeze > requirements.txt to extract added libraries to requirements.txt

9. To format your code you can use:

    ```python
    HTML: python format_html.py
    Python: black .
    ```

10. You can use the following script to add initial data into project:

    ```python
    python manage.py loaddata initial_data.json
    ```

11. Run Coverage:

    ```python
    coverage run --data-file tests/.coverage manage.py test
    coverage json --data-file tests/.coverage -o buf/tests/coverage.json
    coverage report --data-file tests/.coverage
    ```
