from jobs.models import Job, Aggregator, JobSite, Application, Interview
from jobs.forms import JobSiteForm, AggregatorForm, ApplicationForm, InterviewForm

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView


class JobIndexView(generic.ListView):
    template_name = 'jobs/index_cards.html'
    context_object_name = 'jobs_list'

    def get_queryset(self):
        return Job.objects.order_by('date_scraped')

class JobDetailView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        job = get_object_or_404(Job, pk=kwargs['pk'])
        context = {'job': job}
        return render(request, 'jobs/job_detail.html', context)


class JobSiteIndexView(generic.ListView):
    template_name = 'jobs/sites/index.html'
    context_object_name = 'site_list'

    def get_queryset(self):
        return JobSite.objects.all()

class AggregatorIndexView(generic.ListView):
    template_name = 'jobs/aggregators/index.html'
    context_object_name = 'agg_list'

    def get_queryset(self):
        return Aggregator.objects.all()

class ApplicationIndexView(generic.ListView):
    template_name = 'jobs/applications/index.html'
    context_object_name = 'app_list'

    def get_queryset(self):
        return Application.objects.all()

class InterviewIndexView(generic.ListView):
    template_name = 'jobs/interviews/index.html'
    context_object_name = 'interview_list'

    def get_queryset(self):
        return Interview.objects.all()


def new_jobsite(request):
    if request.method == 'POST':
        form = JobSiteForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            search_url = form.cleaned_data['search_url_template']
            jobs_per_page = form.cleaned_data['jobs_per_page']
            page_parameter = form.cleaned_data['page_parameter']
            j = JobSite(
                url=url,
                search_url_template=search_url,
                jobs_per_page=jobs_per_page,
                page_parameter=page_parameter
            )
        j.save()
        return HttpResponseRedirect('/jobs/sites/')
    else:
        form = JobSiteForm()
    return render(request, 'jobs/sites/new.html', {'form': form})

class JobSiteUpdateView(UpdateView):
    model = JobSite
    form_class = JobSiteForm
    template_name = 'jobs/sites/update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/jobs/sites/')

    def dispatch(self, request, *args, **kwargs):
        return super(JobSiteUpdateView, self).dispatch(request, *args, **kwargs)

class JobSiteDeleteView(DeleteView):
    model = JobSite

    def get_success_url(self):
        return reverse('jobs:sites')

    def dispatch(self, request, *args, **kwargs):
        return super(JobSiteDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def new_aggregator(request):
    if request.method == 'POST':
        form = AggregatorForm(request.POST)
        if form.is_valid():
            job_site = form.cleaned_data['job_site']
            keywords = form.cleaned_data['keywords']
            run_schedule = form.cleaned_data['run_schedule']
            archive_raw_html = form.cleaned_data['archive_raw_html']
            send_alerts = form.cleaned_data['send_alerts']
            max_threads = form.cleaned_data['max_threads']
            a = Aggregator(
                job_site=job_site,
                keywords=keywords,
                run_schedule=run_schedule,
                archive_raw_html=archive_raw_html,
                send_alerts=send_alerts,
                max_threads=max_threads
            )
            a.save()
            return HttpResponseRedirect('/jobs/aggregators/')
    else:
        form = AggregatorForm()
    return render(request, 'jobs/aggregators/new.html', {'form': form})

class AggregatorUpdateView(UpdateView):
    model = Aggregator
    form_class = AggregatorForm
    template_name = 'jobs/sites/update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/jobs/sites/')

    def dispatch(self, request, *args, **kwargs):
        return super(AggregatorUpdateView, self).dispatch(request, *args, **kwargs)

class AggregatorDeleteView(DeleteView):
    model = Aggregator

    def get_success_url(self):
        return reverse('jobs:sites')

    def dispatch(self, request, *args, **kwargs):
        return super(AggregatorDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def new_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            a = Application(
                job=form.cleaned_data['job'],
                apply_date=form.cleaned_data['apply_date'],
                status=form.cleaned_data['status'],
                contact=form.cleaned_data['contact'],
                notes=form.cleaned_data['notes']
                )
            a.save()
            return HttpResponseRedirect('/jobs/applications/')
    else:
        form = ApplicationForm()
    return render(request, 'jobs/applications/new.html', {'form': form})


class ApplicationUpdateView(UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'jobs/sites/update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/jobs/applications/')

    def dispatch(self, request, *args, **kwargs):
        return super(ApplicationUpdateView, self).dispatch(request, *args, **kwargs)


class ApplicationDeleteView(DeleteView):
    model = Application

    def get_success_url(self):
        return reverse('jobs:apps')

    def dispatch(self, request, *args, **kwargs):
        return super(ApplicationDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def new_interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            a = Interview(
                application=form.cleaned_data['application'],
                date=form.cleaned_data['date'],
                type=form.cleaned_data['type'],
                contact=form.cleaned_data['contact'],
                notes=form.cleaned_data['notes'],
                status=form.cleaned_data['status']
            )
            a.save()
            return HttpResponseRedirect('/jobs/interviews/')
    else:
        form = InterviewForm()
    return render(request, 'jobs/interviews/new.html', {'form': form})

class InterviewUpdateView(UpdateView):
    model = Interview
    form_class = InterviewForm
    template_name = 'jobs/sites/update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/jobs/interviews/')

    def dispatch(self, request, *args, **kwargs):
        return super(InterviewUpdateView, self).dispatch(request, *args, **kwargs)

class InterviewDeleteView(DeleteView):
    model = Interview

    def get_success_url(self):
        return reverse('jobs:intv')

    def dispatch(self, request, *args, **kwargs):
        return super(InterviewDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
