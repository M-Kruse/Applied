from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'jobs', views.JobViewSet, basename='jobs')
router.register(r'sites', views.JobSiteViewSet)
router.register(r'aggregators', views.AggregatorViewSet)
router.register(r'applications', views.ApplicationViewSet)
router.register(r'interviews', views.InterviewViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
