# Todo App

A simple, modern to-do list application built with Django.

## Features

- ✅ Create, read, update, and delete tasks
- 📊 Task statistics dashboard
- 🏷️ Priority levels (Low, Medium, High)
- 🎨 Clean, responsive UI
- 🔍 Filter tasks by status and priority
- 📈 Coverage tracking for all tests

## Tech Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (default) / PostgreSQL (production)
- **Testing**: pytest, pytest-django, pytest-cov
- **Code Quality**: Black, isort, flake8, pylint

## Project Structure

```
├── todos/                    # Main todo application
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   ├── forms.py              # Form definitions
│   ├── models.py             # Database models
│   ├── test_todos.py         # Unit tests
│   ├── urls.py               # URL routing
│   └── views.py              # View functions
├── todo_project/             # Django project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py               # Root URL configuration
│   └── wsgi.py               # WSGI application
├── tests/                    # Additional tests
├── .github/
│   └── workflows/            # GitHub Actions CI/CD
│       ├── ci-cd.yml         # Main CI/CD pipeline
│       └── code-review.yml   # Code review workflow
├── conftest.py               # pytest configuration
├── pytest.ini                # pytest settings
├── requirements.txt          # Python dependencies
├── manage.py                 # Django management script
└── README.md                 # This file
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser at `http://localhost:8000`

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=todos --cov-report=term-missing

# Run specific test file
pytest todos/test_todos.py -v

# Run with parallel execution
pytest -n auto
```

## Code Quality

```bash
# Format code
black .
isort .

# Check formatting
black --check .
isort --check-only .

# Lint code
flake8 .
pylint todos todo_project

# Security scan
bandit -r todos todo_project
safety check
pip-audit
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment verification.

### Workflows

1. **Lint & Format Check** - Validates code style with Black, isort, flake8, and pylint
2. **Security Scans** - Runs Bandit, Safety, and pip-audit for vulnerability detection
3. **Dependency Analysis** - Checks for circular dependencies and outdated packages
4. **Test Suite** - Runs tests across multiple Python and Django versions
5. **Integration Tests** - Validates the complete application functionality
6. **Build & Package** - Ensures the project builds correctly
7. **Quality Gate** - Final verification before code merge

### Trigger Conditions

- Push to `main`, `develop`, or feature/fix branches
- Pull requests to `main`
- Manual workflow dispatch

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DJANGO_SECRET_KEY` | Django secret key | `django-insecure-dev-key...` |
| `DJANGO_DEBUG` | Enable debug mode | `True` |
| `DJANGO_ALLOWED_HOSTS` | Allowed hosts (comma-separated) | `localhost,127.0.0.1` |
| `DATABASE_URL` | Database connection URL | SQLite (local) |

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and add tests
3. Ensure all tests pass: `pytest`
4. Format your code: `black . && isort .`
5. Commit your changes: `git commit -m "Add your feature"`
6. Push to the branch: `git push origin feature/your-feature`
7. Open a Pull Request

## License

MIT License - see LICENSE file for details
