from django.forms import ModelForm
from TUTRReg.models import Event, Class, Person


class EventForm(ModelForm):
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


class ClassForm(ModelForm):
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


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('sca_name',
                  'first_name',
                  'last_name',
                  'branch_id',
                  'position',
                  'teacher')


