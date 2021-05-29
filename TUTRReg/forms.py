from django.forms import ModelForm, BaseModelFormSet, BooleanField, modelformset_factory, EmailField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from TUTRReg.models import Event, Class, Person, Attendance


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
                  'teacher',
                  'minor',
                  'guardian',
                  'active')


class AttendanceForm(ModelForm):
    attended = BooleanField()
    passed = BooleanField

    class Meta:
        model = Attendance
        fields = ('person_id',
                  'attended',
                  'passed')

    def __init__(self, *args, **kwargs):
        self.session_id = kwargs['session_id']
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['person_id'].queryset = Attendance.objects.filter(session_id=self.session_id)


BaseAttendanceFormSet = modelformset_factory(Attendance, form=AttendanceForm, extra=1, can_delete=False)


class AttendanceFormSet(BaseAttendanceFormSet):
    def __init__(self, *args, **kwargs):
        self.person_id = kwargs.pop('person_id')
        super(AttendanceFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

    def _construct_form(self, *args, **kwargs):
        kwargs[person_id] = self.person_id
        return super(AttendanceFormSet, self)._construct_form(*args, **kwargs)


class RegistrationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
