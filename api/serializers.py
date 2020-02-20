from rest_framework import serializers
from jobs.models import Job, JobSite, Aggregator, Application, Interview, Description
from django.contrib.auth.models import User

class DescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Description
        fields = [
            'text'
        ]


class JobSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    description = DescriptionSerializer()
    class Meta:
        model = Job
        fields = [
                    'owner',
                    'job_site',
                    'keywords',
                    'title',
                    'location',
                    'company',
                    'date_posted',
                    'date_scraped',
                    'url',
                    'description'
                ]


    def create(self, validated_data):
        print("DATA:",validated_data)
        #desc_data = validated_data.pop('model')
        desc_serializer = DescriptionSerializer(data=validated_data['description'])
        desc_serializer.is_valid(raise_exception=True)
        validated_data['description'] = desc_serializer.save()
        instance = super().create(validated_data)
        return instance

class JobSiteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = JobSite
        fields = [
                    'owner',
                    'url',
                    'date_created',
                    'search_url_template',
                    'jobs_per_page',
                    'page_parameter'
                ]

class AggregatorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Aggregator
        fields = [
                    'owner',
                    'job_site',
                    'max_threads',
                    'run_schedule',
                    'archive_raw_html',
                    'send_alerts',

                ]

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Application
        fields = [
                    'create_date',
                    'apply_date',
                    'owner',
                    'job',
                    'status',
                    'contact',
                    'notes'
                ]

class InterviewSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Interview
        fields = [
                    'owner',
                    'application',
                    'date',
                    'type',
                    'contact',
                    'notes',
                    'date_created'
                ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='job-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'jobs']