# core/urls.py

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# API Routes
router.register('users', views.UserViewSet, basename='user')
router.register('experts', views.ExpertProfileViewSet, basename='expert-profile')
router.register('workouts', views.WorkoutPlanViewSet, basename='workout')
router.register('user-activities', views.UserWorkoutActivityViewSet, basename='user-activity')
router.register('likes', views.LikeViewSet, basename='like')
router.register('comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', views.CustomAuthToken.as_view(), name='api-token-auth')
]