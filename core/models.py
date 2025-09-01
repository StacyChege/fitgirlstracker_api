from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Experts profile 
class ExpertProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    bio = models.TextField(blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Expert: {self.user.username} ({'Verified' if self.verified else 'Unverified'})"
    

# Workout Choices part

GOAL_CHOICES = (
    ('ABS', 'Abs'),
    ('BOOTY', 'Booty'),
    ('ARMS', 'Arms'),
    ('FULL_BODY', 'Full-Body'),
)

DIFFICULTY_CHOICES = (
    ('BEGINNER', 'Beginner'),
    ('INTERMEDIATE', 'Intermediate'),
    ('ADVANCED', 'Advanced'),
)


class WorkoutPlan(models.Model):
        title = models.CharField(max_length=255)
        goal = models.CharField(max_length=255, choices=GOAL_CHOICES)
        difficulty = models.CharField(max_length=255, choices=DIFFICULTY_CHOICES)
        description = models.TextField()
        posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans')
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title
        
# Choices for the UserWorkoutActivity status. (If completed or in Progress)
USER_WORKOUT_ACTIVITY_STATUS_CHOICES = (
    ('COMPLETED', 'Completed'),
    ('IN_PROGRESS', 'In Progress'),
)


# Model to track a normal user's progress on a workout plan.
class UserWorkoutActivity(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_activities')
     workout = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='user_activities')
     status = models.CharField(max_length=15, choices=USER_WORKOUT_ACTIVITY_STATUS_CHOICES)
     data_logged = models.DateField(auto_now_add=True)
     notes = models.TextField(blank=True, null=True)

     def __str__(self):
         return f"{self.user.username} - {self.workout.title} ({self.status})"


# Model to track which user liked which workout
class Like(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     workout = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
     

     class Meta:
         unique_together = ('user', 'workout') # Ensure a user can like a workout only once

     def __str__(self):
         return f"{self.user.username} liked {self.workout.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.workout.title}"