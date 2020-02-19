from django.urls import path, include
from django.conf.urls import url
#from rest_framework.routers import DefaultRouter
from jobs import views

urlpatterns = [
	url(r'', login_required(views.DashboardIndexView.as_view()), name='home'),
	#path('/jobs/', views.JobIndexView.as_view(), name="jobs"),
]l