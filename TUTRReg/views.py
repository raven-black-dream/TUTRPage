from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views import generic, View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.db.models import Q

from .models import Event, Session, Class, Course, Attendance, Person
from .forms import EventForm, ClassForm, PersonForm
from datetime import datetime
# Create your views here.


def register(request, *args, **kwargs):
    if request.POST:
        user = request.user.person_id
        session = Session.objects.get(pk=kwargs['session_id'])
        registration = Attendance.objects.create(session_id=session, person_id=user)
        event = session.event_id.pk
        registration.save()

    return HttpResponseRedirect(reverse('TUTRReg:event_detail'), args=(event,))


class CreateEventView(generic.CreateView):
    template_name = 'TUTRReg/edit_event.html'
    form_class = EventForm


class UpdateEventView(generic.UpdateView):
    model = Event
    template_name = 'TUTRReg/edit_event.html'
    form_class = EventForm


class CreateClassView(generic.CreateView):
    template_name = 'TUTRReg/edit_class.html'
    form_class = ClassForm


class UpdateClassView(generic.UpdateView):
    model = Class
    template_name = 'TUTRReg/edit_class.html'
    form_class = ClassForm


class CreatePersonView(generic.CreateView):
    template_name = 'TUTRReg/edit_person.html'
    form_class = PersonForm


class UpdatePersonView(generic.UpdateView):
    model = Person
    template_name = 'TUTRReg/edit_person.html'
    form_class = PersonForm


class SessionView(generic.ListView):
    model = Event
    template_name = 'TUTRReg/sessions.html'
    context_object_name = 'EventList'

    def get_context_data(self, *, object_list=None, **kwargs):
        one_year_ago = timezone.now() - timezone.timedelta(days=365)
        context = super(SessionView, self).get_context_data(**kwargs)
        context['past_events'] = Event.objects.filter(start_date__gte=one_year_ago, start_date__lte=timezone.now())
        context['future_events'] = Event.objects.filter(start_date__gte=timezone.now())
        return context


class EventDetail(generic.DetailView):
    model = Event
    template_name = 'TUTRReg/event.html'
    context_object_name = 'EventDetailList'

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['class_list'] = Session.objects.filter(event_id=self.kwargs['pk']).select_related("class_id")
        event_end_date = Session.objects.filter(event_id=self.kwargs['pk']).values('event_id__end_date').first()
        end_date = event_end_date['event_id__end_date']
        context['open'] = end_date >= timezone.now().date()
        return context


class ClassDetail(generic.DetailView):
    model = Class
    template_name = 'TUTRReg/class.html'
    context_object_name = 'ClassDetails'

    def get_context_data(self, **kwargs):
        context = super(ClassDetail, self).get_context_data(**kwargs)
        return context


class EventClassDetail(generic.DetailView):
    model = Class
    template_name = 'TUTRReg/event_class_detail.html'
    context_object_name = 'EventClassDetails'


class CourseDetail(generic.DetailView):
    model = Course
    template_name = 'TUTRReg/course.html'
    context_object_name = 'CourseDetails'

    def get_context_data(self, **kwargs):
        context = super(CourseDetail, self).get_context_data(**kwargs)
        context['class_list'] = Class.objects.filter(course_id=self.kwargs['pk'])
        return context


class LandingView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, request, *args, **kwargs):
        context_parts = {'Student': [],
                         'Dean': [],
                         'Registrar': [],
                         'Head Registrar': [],
                         'Governor': []}

        context = {}
        return render(request, 'TUTRReg/landing.html', context=context)


class AddClassView(generic.ListView):
    template_name = 'TUTRReg/add_class.html'
    model = Session

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            object_list = Class.objects.all()
        else:
            object_list = Class.objects.filter(Q(class_name__icontains=query))
        return object_list


class AttendanceView(generic.ListView):
    model = Attendance


