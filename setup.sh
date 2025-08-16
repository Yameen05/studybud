#!/bin/bash

echo "Setting up StudyBud Django Project..."

# Activate virtual environment
if [ -d "env" ]; then
    echo "Activating virtual environment..."
    source env/bin/activate
else
    echo "Creating virtual environment..."
    python3 -m venv env
    source env/bin/activate
fi

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Check for any issues
echo "Checking Django configuration..."
python manage.py check

echo "Setup complete! Run 'python manage.py runserver' to start the development server."
echo "Don't forget to activate the virtual environment with 'source env/bin/activate'"