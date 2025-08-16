# StudyBud - Django Study Room Application

A Django-based web application for creating and managing study rooms where users can discuss topics and share knowledge.

## Features

- User authentication with email-based login
- Create and join study rooms
- Real-time messaging in rooms
- Topic-based room organization
- User profiles with avatars and bio
- REST API endpoints
- Responsive design

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Create sample data (optional):
   ```bash
   python manage.py create_sample_data
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000` in your browser

## API Endpoints

- `GET /api/` - List all available API routes
- `GET /api/rooms/` - Get all rooms
- `GET /api/rooms/<id>/` - Get specific room details

## Project Structure

- `base/` - Main Django app containing models, views, and templates
- `studybud/` - Django project settings and configuration
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates
- `env/` - Virtual environment (not tracked in git)

## Models

- **User** - Custom user model with email authentication
- **Room** - Study rooms with topics and participants
- **Topic** - Categories for organizing rooms
- **Message** - Messages posted in rooms

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request