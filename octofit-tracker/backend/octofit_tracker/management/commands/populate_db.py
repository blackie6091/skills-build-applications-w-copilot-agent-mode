from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User.objects.create(email="thundergod@mhigh.edu", name="Thunder God", age=25),
            User.objects.create(email="metalgeek@mhigh.edu", name="Metal Geek", age=23),
            User.objects.create(email="zerocool@mhigh.edu", name="Zero Cool", age=24),
            User.objects.create(email="crashoverride@mhigh.edu", name="Crash Override", age=22),
            User.objects.create(email="sleeptoken@mhigh.edu", name="Sleep Token", age=26)
        ]

        # Create teams
        teams = [
            Team.objects.create(name="Blue Team", members=["Thunder God", "Metal Geek"]),
            Team.objects.create(name="Gold Team", members=["Zero Cool", "Crash Override", "Sleep Token"])
        ]

        # Create activities
        activities = [
            Activity.objects.create(user="Thunder God", activity_type="Cycling", duration=30),
            Activity.objects.create(user="Metal Geek", activity_type="Crossfit", duration=45),
            Activity.objects.create(user="Zero Cool", activity_type="Running", duration=60),
            Activity.objects.create(user="Crash Override", activity_type="Strength", duration=40),
            Activity.objects.create(user="Sleep Token", activity_type="Swimming", duration=50)
        ]

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard.objects.create(user="Thunder God", score=100),
            Leaderboard.objects.create(user="Metal Geek", score=90),
            Leaderboard.objects.create(user="Zero Cool", score=95),
            Leaderboard.objects.create(user="Crash Override", score=85),
            Leaderboard.objects.create(user="Sleep Token", score=80)
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name="Morning Cycling", description="30-minute cycling session"),
            Workout.objects.create(name="Crossfit Challenge", description="High-intensity interval training"),
            Workout.objects.create(name="Track Running", description="60-minute endurance run"),
            Workout.objects.create(name="Strength Training", description="Full body workout with weights"),
            Workout.objects.create(name="Swim Practice", description="50-minute pool session")
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
