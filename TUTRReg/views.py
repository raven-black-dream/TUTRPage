from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views import generic, View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Event, Session, Class, Course, Attendance
# Create your views here.


def register(request, *args, **kwargs):
    if request.POST:
        user = request.user.person_id
        session = Session.objects.get(pk=kwargs['session_id'])
        registration = Attendance.objects.create(session_id=session, person_id=user)
        event = session.event_id.pk
        registration.save()

    return HttpResponseRedirect(reverse('TUTRReg:event_detail'), args=(event,))


class SessionView(generic.ListView):
    model = Event
    template_name = 'TUTRReg/sessions.html'
    context_object_name = 'EventList'

    def get_queryset(self):
        return Event.objects.filter(start_date__gte=timezone.now())


class EventDetail(generic.DetailView):
    model = Event
    template_name = 'TUTRReg/event.html'
    context_object_name = 'EventDetailList'

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['class_list'] = Session.objects.filter(event_id=self.kwargs['pk']).select_related("class_id")
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

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'TUTRReg/landing.html', context=context)

