from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ExpertProfile, WorkoutPlan, UserWorkoutActivity, Like, Comment


# ExpertProfile Serializer
class ExpertProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExpertProfile
        fields = 'certificate', 'bio', 'verified'

# User Serializer
# Includes the ExpertProfile for easy access in the API
class UserSerializer(serializers.ModelSerializer):

    expert_profile = ExpertProfileSerializer(read_only=True) # Can be read from the API but not set directly when creating or updating a user.

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'expert_profile']

# Serializer for user creation to handle the password.
class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['username' 'email' 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    


# WorkoutPlan Serializer
"""
Serializer for the Workout model.
Handles CRUD operations and shows the expert who posted the workout.
"""
class WorkoutPlanSerializer(serializers.ModelSerializer):
    
    # Use the ExpertProfileSerializer to display the expert's information
    posted_by = ExpertProfileSerializer(read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'title', 'goal', 'difficulty', 'description', 'posted_by', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

# UserWorkoutActivity Serializer
"""
Serializer for the UserWorkoutActivity model.
Handles CRUD operations and shows the user and workout information.
"""
class UserWorkoutActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserWorkoutActivity
        fields = ['id', 'user', 'workout', 'status', 'date_logged', 'notes']
        read_only_fields = ['user', 'date_logged']


# LikeSerializer
class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id', 'user', 'workout']
        read_only_fields = ['created_at']


# CommentSerializer
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'user', 'workout', 'text', 'created_at']
        read_only_fields = ['user', 'created_at']