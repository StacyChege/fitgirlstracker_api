from django.contrib import admin
from .models import ExpertProfile, WorkoutPlan, UserWorkoutActivity, Like, Comment

# Register your models here.
admin.site.register(ExpertProfile)
admin.site.register(WorkoutPlan)
admin.site.register(UserWorkoutActivity)
admin.site.register(Like)
admin.site.register(Comment)
