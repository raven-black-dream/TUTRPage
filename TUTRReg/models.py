from django.db import models
from django.contrib.auth.models import AbstractUser
import django.core.validators as val
from simple_history.models import HistoricalRecords

# Create your models here.


class Principality(models.Model):
    principality_name = models.CharField(max_length=15)

    def __str__(self):
        return self.principality_name


class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    principality = models.ForeignKey(Principality, on_delete=models.PROTECT)

    def __str__(self):
        return self.branch_name


class Person(models.Model):
    sca_name = models.CharField(null=True, max_length=100)
    first_name = models.CharField(null=True, max_length=100)
    last_name = models.CharField(null=True, max_length=100)
    branch_id = models.ForeignKey(Branch, on_delete=models.PROTECT)
    joined_date = models.DateField('Date Joined', blank=True, null=True)
    active = models.BooleanField()
    position = models.CharField(max_length=100, blank=True)
    teacher = models.BooleanField()
    minor = models.BooleanField(blank=True)
    guardian = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.sca_name


class User(AbstractUser):
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT, null=True, blank=True)
    pass


class DegreeType(models.Model):
    type_name = models.CharField(max_length=100)
    core_credits = models.IntegerField()
    extra_credits = models.IntegerField()

    def __str__(self):
        return self.type_name


class Degree(models.Model):
    degree_name = models.CharField(max_length=100)
    degree_cd = models.ForeignKey(DegreeType, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.degree_name


class Major(models.Model):
    major_name = models.CharField(max_length=100)
    degree_cd = models.ForeignKey(Degree, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.major_name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    hours = models.DecimalField(max_digits=3, decimal_places=1)
    credits = models.IntegerField()
    approved = models.BooleanField()
    history = HistoricalRecords()

    def __str__(self):
        return self.course_name


class Class(models.Model):
    class_name = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    min_participants = models.IntegerField()
    max_participants = models.IntegerField()
    travel = models.BooleanField()
    handouts = models.BooleanField()
    student_reqs = models.TextField(null=True)
    loc_reqs = models.TextField(null=True)
    description = models.TextField(null=True)
    pre_reqs = models.TextField(null=True)
    teacher = models.ForeignKey(Person, on_delete=models.PROTECT)
    approved = models.BooleanField()
    history = HistoricalRecords()

    def __str__(self):
        return self.class_name


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    tutr_surcharge = models.DecimalField(max_digits=5, decimal_places=2)
    branch_id = models.ForeignKey(Branch, on_delete=models.PROTECT)
    dean = models.ForeignKey(Person, null=True, on_delete=models.PROTECT)
    location_name = models.CharField(null=True, max_length=100)
    apt_num = models.CharField(null=True, max_length=10)
    street = models.CharField(null=True, max_length=200)
    city = models.CharField(null=True, max_length=100)
    postal_cd = models.CharField(null=True, max_length=7, validators=[val.RegexValidator(
        regex=r'^\d{5}-\d{4}|\d{5}|[A-Z]\d[A-Z] \d[A-Z]\d$',
        message='You have entered an invalid Postal Code. Please enter a valid Canadian or US Postal Code')])
    closed = models.BooleanField()
    history = HistoricalRecords()
    approved = models.BooleanField()

    def __str__(self):
        return self.event_name


class Session(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.PROTECT)
    event_id = models.ForeignKey(Event, on_delete=models.PROTECT)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return str(self.pk)


class Attendance(models.Model):
    session_id = models.ForeignKey(Session, on_delete=models.PROTECT)
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT)
    attended = models.BooleanField(null=True, blank=True)
    passed = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return '{0}: {1}'.format(self.session_id.class_id.class_name, self.person_id.sca_name)

