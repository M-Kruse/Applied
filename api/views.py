from jobs.models import Job, JobSite, Aggregator, Application, Interview
from api.serializers import JobSerializer, JobSiteSerializer, AggregatorSerializer
from api.serializers import ApplicationSerializer, InterviewSerializer
from api.serializers import UserSerializer
from api.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import viewsets

from django.contrib.auth.models import User

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'job-list': reverse('job-list', request=request, format=format)
    })

class JobViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class JobSiteViewSet(viewsets.ModelViewSet):
    queryset = JobSite.objects.all()
    serializer_class = JobSiteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AggregatorViewSet(viewsets.ModelViewSet):

    queryset = Aggregator.objects.all()
    serializer_class = AggregatorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ApplicationViewSet(viewsets.ModelViewSet):

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class InterviewViewSet(viewsets.ModelViewSet):

    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
