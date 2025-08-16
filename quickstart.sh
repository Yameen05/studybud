#!/bin/bash

echo "🚀 StudyBud Quick Start"
echo "======================"

# Check if virtual environment exists
if [ ! -d "env" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv env
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source env/bin/activate

# Install requirements
echo "📚 Installing requirements..."
pip install -r requirements.txt

# Run migrations
echo "🗄️  Setting up database..."
python manage.py makemigrations
python manage.py migrate

# Create sample data
echo "🎯 Creating sample data..."
python manage.py create_sample_data

# Check system
echo "✅ Running system check..."
python manage.py check

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the server:"
echo "1. Activate virtual environment: source env/bin/activate"
echo "2. Run server: python manage.py runserver"
echo "3. Visit: http://127.0.0.1:8000"
echo ""
echo "Demo login: demo@example.com / demo123"