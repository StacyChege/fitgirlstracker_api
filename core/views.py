from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from .models import ExpertProfile, WorkoutPlan, UserWorkoutActivity, Like, Comment
from .serializers import (
    UserSerializer, UserCreationSerializer, ExpertProfileSerializer, 
    WorkoutPlanSerializer, UserWorkoutActivitySerializer, LikeSerializer,
    CommentSerializer
)

from .permissions import IsExpert, IsOwnerOrAdmin

# User and Authentication Views
# For handling user registration and managing their profiles
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        # Custom permissions based on action
        if self.action == 'create':
            self.permission_classes = [AllowAny] # Allow anyone to sign up
        else:
            self.permission_classes = [IsAuthenticated] # Require authentication for other actions
        return [permission() for permission in self.permission_classes]

    # Different serializer for user creation
    def get_serializer_class(self): 
        if self.action == 'create':
            return UserCreationSerializer
        return UserSerializer
    

# Handles user login and token generation
class CustomAuthToken(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# Expert Profile View
class ExpertProfileViewSet(viewsets.ModelViewSet):
    queryset = ExpertProfile.objects.all()
    serializer_class = ExpertProfileSerializer
    permission_classes = [IsExpert] # Only experts can manage expert profiles


# Workout Plan View
# Handles CRUD for workout plans.
# Only experts can create, update, or delete workout plans.
class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        # Allow any authenticated user to list and retrieve (view) workout plans
        if self.action in ['list', 'retrieve', 'like', 'comments']:
            permission_classes = [IsAuthenticated]
        # Only experts can create, update, or delete workout plans
        else:
            permission_classes = [IsAuthenticated, IsExpert]
        return [permission() for permission in permission_classes]

    # Special action for liking/unliking a workout
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        workout = self.get_object()
        user = request.user

        # Check if the user has already liked the workout
        try:
            like = Like.objects.get(user=user, workout=workout)
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            Like.objects.create(user=user, workout=workout)
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)

    # Action for viewing/posting comments on a workout
    @action(detail=True, methods=['get', 'post'])
    def comments(self, request, pk=None):
        workout = self.get_object()
        if request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, workout=workout)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # This part handles the GET request for comments
        comments = workout.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


# User Activities Views
class UserWorkoutActivityViewSet(viewsets.ModelViewSet):
    serializer_class = UserWorkoutActivitySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        return UserWorkoutActivity.objects.filter(user=self.request.user)
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # Automatically adds the logged-in user to the record

    # Custom endpoint to view a user's workout history
    @action(detail=False, methods=['get'], url_path='history')
    def history(self, request):
        activities = self.get_queryset().order_by('-date_logged')
        serializer = UserWorkoutActivitySerializer(activities, many=True)
        return Response(serializer.data)
    

# Like View
class LikeViewSet(viewsets.ModelViewSet): # Handles adding likes
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # Automatically adds the logged-in user to the record


# Comment View
class CommentViewSet(viewsets.ModelViewSet): # Handles posting and retrieving comments
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # Automatically adds the logged-in user to the record