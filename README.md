
# Django Email Sender

A beginner-friendly Django project for preparing emails through a web form and learning DevOps practices.

## Features
- Email form with recipient, subject, and message fields
- Email address validation
- Django email framework
- Automated tests for valid and invalid submissions
- GitHub Actions continuous integration (CI)

## Technologies
- Python 3.10
- Django 5.2
- Git and GitHub
- GitHub Actions

## Run locally
1. Activate the virtual environment.
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Check the project: `python manage.py check`
5. Run tests: `python manage.py test`
6. Start the server: `python manage.py runserver`
7. Open http://127.0.0.1:8000/

## Email testing
The development email backend prints email contents in the terminal. Automated tests use an in-memory email backend. This project does not currently send real emails.

## Continuous Integration
GitHub Actions will install dependencies and run Django checks and tests on pushes and pull requests.
