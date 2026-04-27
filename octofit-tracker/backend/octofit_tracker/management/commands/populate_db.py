from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        with transaction.atomic():
            # Clear existing data
            User.objects.all().delete()
            Team.objects.all().delete()
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()

            # Create Teams
            marvel = Team.objects.create(name='Marvel')
            dc = Team.objects.create(name='DC')

            # Create Users
            ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
            captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
            batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
            superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

            # Create Activities
            Activity.objects.create(user=ironman, type='run', duration=30)
            Activity.objects.create(user=captain, type='cycle', duration=45)
            Activity.objects.create(user=batman, type='swim', duration=60)
            Activity.objects.create(user=superman, type='run', duration=50)

            # Create Workouts
            Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
            Workout.objects.create(name='Strength Training', description='Strength for all heroes')

            # Create Leaderboard
            Leaderboard.objects.create(user=ironman, score=100)
            Leaderboard.objects.create(user=captain, score=90)
            Leaderboard.objects.create(user=batman, score=95)
            Leaderboard.objects.create(user=superman, score=98)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
