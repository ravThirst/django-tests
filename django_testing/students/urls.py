from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CoursesViewSet

router = DefaultRouter()
router.register("courses", CoursesViewSet, basename='courses')

app_name = 'students'
urlpatterns = [
    path('', include(router.urls))
]
