from django.urls import path, include
from django.conf.urls import url
from jobs import views
from django.contrib.auth.decorators import login_required

app_name = "jobs"
# The API URLs are now determined automatically by the router.
urlpatterns = [
	#path('aggregators/', views.AggregatorIndexView.as_view(), name="agg"),
	path('detail/<int:pk>', login_required(views.JobDetailView.as_view()), name="detail"),
	path('sites/', login_required(views.JobSiteIndexView.as_view()), name="sites"),
	path('sites/new/', login_required(views.new_jobsite), name="new_js"),
	path('sites/edit/<int:pk>', login_required(views.JobSiteUpdateView.as_view()), name="edit_js"),
	path('sites/delete/<int:pk>', login_required(views.JobSiteDeleteView.as_view()), name="del_js"),
	#path('sites/delete/<int:pk>', views.JobSiteDeleteView.as_view(), name="del_js"),
	path('aggregators/', login_required(views.AggregatorIndexView.as_view()), name='agg'),
	path('aggregators/new/', login_required(views.new_aggregator), name='new_agg'),
	path('aggregators/edit/<int:pk>/', login_required(views.AggregatorUpdateView.as_view()), name='edit_agg'),
	path('aggregators/delete/<int:pk>/', login_required(views.AggregatorDeleteView.as_view()), name='del_agg'),
	path('applications/', login_required(views.ApplicationIndexView.as_view()), name="apps"),
	path('applications/new/', login_required(views.new_application), name="new_app"),
	path('applications/edit/<int:pk>', login_required(views.ApplicationUpdateView.as_view()), name="edit_app"),
	path('applications/delete/<int:pk>', login_required(views.ApplicationDeleteView.as_view()), name="del_app"),
	path('interviews/', login_required(views.InterviewIndexView.as_view()), name="intv"),
	path('interviews/new/', login_required(views.new_interview), name="new_intv"),
	path('interviews/edit/<int:pk>', login_required(views.InterviewUpdateView.as_view()), name="edit_intv"),
	path('interviews/delete/<int:pk>', login_required(views.InterviewDeleteView.as_view()), name="del_intv"),
	path('', login_required(views.JobIndexView.as_view()), name='jobs'),
    
]	