from django.contrib import admin
from django.urls import path, include
from dashboard import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

	path('', login_required(views.DashboardIndexView.as_view())),
    path('jobs/', include('jobs.urls')),
    path('api/', include('api.urls')),
    path('resume/', include('resume.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
