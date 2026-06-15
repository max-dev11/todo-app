# Contributing to Todo App

Thank you for considering contributing to the Todo App! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How Can I Contribute?

### Reporting Bugs

Before submitting a bug report:
1. Check the existing issues to avoid duplicates
2. Update your packages to the latest versions
3. Provide clear reproduction steps

When submitting a bug report, include:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment (OS, Python version, Django version)

### Suggesting Enhancements

We welcome enhancement suggestions! Please:
1. Check existing issues first
2. Clearly describe the feature and its benefits
3. Provide use case examples

### Pull Requests

1. **Branch Naming**
   - Feature branches: `feature/description`
   - Bug fixes: `fix/description`
   - Documentation: `docs/description`

2. **Development Setup**
   ```bash
   # Clone and setup
   git clone <repo>
   cd todo-app
   python -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run migrations
   python manage.py migrate
   
   # Verify tests pass
   pytest
   ```

3. **Coding Standards**
   - Follow PEP 8 guidelines
   - Use Black for code formatting (line-length: 120)
   - Use isort for import sorting
   - Write meaningful commit messages
   - Add tests for new functionality

4. **Before Submitting**
   - Run the full test suite: `pytest`
   - Format your code: `black . && isort .`
   - Lint your code: `flake8 .`
   - Check for security issues: `bandit -r .`

5. **Commit Message Format**
   ```
   type(scope): description
   
   [optional body]
   
   [optional footer]
   ```
   
   Types:
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation changes
   - `style`: Formatting, no code change
   - `refactor`: Code refactoring
   - `test`: Adding tests
   - `chore`: Maintenance tasks

6. **Pull Request Process**
   - Update documentation if needed
   - Add tests for new features
   - Ensure CI/CD passes
   - Request review from maintainers

## Development Workflow

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Add and commit your changes
5. Push to your fork
6. Open a Pull Request

## Testing Guidelines

- All new features must include tests
- All tests must pass before merging
- Aim for meaningful test coverage
- Test edge cases and error conditions

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=todos --cov-report=term-missing

# Run specific tests
pytest todos/test_todos.py::TestTaskModel -v
```

## Code Review Process

All submissions require review. We use GitHub Pull Requests for this purpose.

During review, maintainers may:
- Request changes
- Suggest improvements
- Ask questions

Please be responsive to feedback and patient during the review process.

## Questions?

Feel free to:
- Open an issue for questions
- Check existing documentation
- Contact maintainers

## Attribution

This Contributing Guide is adapted from various open source contributing guides.
