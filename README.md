# Django Project

A Django project for Python learning.

## Git Clone

To clone this repository, use the following command:

```bash
git clone https://github.com/kapoordev2022/python-learning.git
```

Or if you need to use a personal access token:

```bash
git clone https://YOUR_TOKEN@github.com/kapoordev2022/python-learning.git
```

After cloning, navigate to the project directory:

```bash
cd python-learning
```

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

## Project Structure

- `python-learning/` - Python learning modules and exercises

## Notes

- Make sure to activate your virtual environment before running commands
- The `.gitignore` file is configured to exclude environment files, cache files, CSV files, and other common development artifacts
