from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'sites', views.JobSiteViewSet)
router.register(r'aggregators', views.AggregatorViewSet)
router.register(r'applications', views.ApplicationViewSet)
router.register(r'interviews', views.InterviewViewSet)
#router.register(r'users', views.UserViewSet)




# The API URLs are now determined automatically by the router.
urlpatterns = [
	path('', include(router.urls)),
	#url(r'', views.JobIndexView.as_view(), name='jobs'),
]	