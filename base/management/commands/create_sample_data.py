from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from base.models import Topic, Room, Message

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample data for testing'

    def handle(self, *args, **options):
        # Create sample topics
        topics_data = [
            'Python', 'JavaScript', 'Django', 'React', 'Machine Learning',
            'Web Development', 'Data Science', 'Mobile Development'
        ]
        
        topics = []
        for topic_name in topics_data:
            topic, created = Topic.objects.get_or_create(name=topic_name)
            topics.append(topic)
            if created:
                self.stdout.write(f'Created topic: {topic_name}')

        # Create sample users
        if not User.objects.filter(email='demo@example.com').exists():
            demo_user = User.objects.create_user(
                username='demo',
                email='demo@example.com',
                password='demo123'
            )
            demo_user.bio = 'Demo user for testing'
            demo_user.save()
            self.stdout.write('Created demo user: demo@example.com')
        else:
            demo_user = User.objects.get(email='demo@example.com')

        # Create sample rooms
        sample_rooms = [
            {
                'name': 'Python Basics Discussion',
                'description': 'Learn Python fundamentals together',
                'topic': topics[0]
            },
            {
                'name': 'Django Best Practices',
                'description': 'Share Django tips and tricks',
                'topic': topics[2]
            },
            {
                'name': 'JavaScript Study Group',
                'description': 'Modern JavaScript concepts and frameworks',
                'topic': topics[1]
            }
        ]

        for room_data in sample_rooms:
            room, created = Room.objects.get_or_create(
                name=room_data['name'],
                defaults={
                    'host': demo_user,
                    'topic': room_data['topic'],
                    'description': room_data['description']
                }
            )
            if created:
                self.stdout.write(f'Created room: {room_data["name"]}')

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )