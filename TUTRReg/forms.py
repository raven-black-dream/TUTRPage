from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from TUTRReg.models import Event, Class, Course, Person, Attendance, Session
from .layout import *


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name',
                  'start_date',
                  'end_date',
                  'tutr_surcharge',
                  'branch_id',
                  'location_name',
                  'apt_num',
                  'street',
                  'city',
                  'postal_cd')


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('class_name',
                  'course_id',
                  'cost',
                  'min_participants',
                  'max_participants',
                  'travel',
                  'handouts',
                  'student_reqs',
                  'loc_reqs',
                  'description',
                  'pre_reqs',
                  'teacher')

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        self.fields['course_id'].queryset = Course.objects.order_by('course_name')


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('sca_name',
                  'first_name',
                  'last_name',
                  'branch_id',
                  'position',
                  'teacher',
                  'minor',
                  'guardian',
                  'active')


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['start_time', 'end_time', 'class_id', 'event_id']

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('class_id'),
                Field('event_id'),
                Field('start_time'),
                Field('end_time'),
                Fieldset('Students',
                         Formset('students')),
                HTML('<br>'),
                ButtonHolder(Submit('submit', 'save'))
            )
        )


AttendanceFormSet = inlineformset_factory(Session, Attendance,
                                          fields=('person_id', 'attended', 'passed',), can_delete=False, extra=0)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
