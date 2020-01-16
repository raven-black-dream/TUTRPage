from django.contrib import admin
from .models import Principality, Branch, Degree, DegreeType, Major, \
    Course, Person, Event, Class, Session, User, Attendance
# Register your models here.
admin.site.register(Principality)
admin.site.register(Branch)
admin.site.register(Degree)
admin.site.register(DegreeType)
admin.site.register(Major)
admin.site.register(Course)
admin.site.register(Person)
admin.site.register(Event)
admin.site.register(Class)
admin.site.register(Session)
admin.site.register(User)
admin.site.register(Attendance)
