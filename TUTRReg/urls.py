"""TUTRPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views
app_name = 'TUTRReg'
urlpatterns = [
    path('', TemplateView.as_view(template_name='TUTRReg/index.html'), name='index'),
    path('faculty/', TemplateView.as_view(template_name='TUTRReg/faculty.html'), name='faculty'),
    path('degrees/', TemplateView.as_view(template_name='TUTRReg/degrees.html'), name='degrees'),
    path('degrees/list', views.DegreeList.as_view(), name='degree_list'),
    path('degrees/<int:pk>', views.DegreeDetail.as_view(), name='degree_detail'),
    path('faq/', TemplateView.as_view(template_name='TUTRReg/faq.html'), name='faq'),
    path('documents/', TemplateView.as_view(template_name='TUTRReg/docs.html'), name='documents'),
    path('links/', TemplateView.as_view(template_name='TUTRReg/links.html'), name='links'),
    path('majors/list', views.MajorList.as_view(), name='major_list'),
    path('majors/<int:pk>', views.MajorDetail.as_view(), name='major_detail'),
    path('sessions/', views.SessionView.as_view(), name='sessions'),
    path('sessions/<int:pk>/', views.EventDetail.as_view(), name='event_detail'),
    path('sessions/<int:session_id>/<int:pk>/', views.EventClassDetail.as_view(), name='event_class_detail'),
    path('classes/<int:pk>/', views.ClassDetail.as_view(), name='class_detail'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='TUTRReg/login.html')),
    path('accounts/register', views.register_user, name='user_registration'),
    path('landing/', views.landing, name='landing'),
    path('sessions/<int:session_id>/<int:class_id>/register/', views.register, name='register'),
    path('sessions/new', views.CreateEventView.as_view(), name='new_event'),
    path('sessions/<int:pk>/edit/', views.UpdateEventView.as_view(), name='edit_event'),
    path('classes/new/', views.CreateClassView.as_view(), name='new_class'),
    path('person/new', views.CreatePersonView.as_view(), name='create_person'),
    path('classes/<int:pk>/edit/', views.UpdateClassView.as_view, name='edit_class'),
    path('sessions/<int:event_id>/add/classes/', views.AddClassView.as_view(), name='add_classes'),
    path('sessions/<int:session_id>/add/', views.AddPersonView.as_view(), name='add_person'),
    path('sessions/<int:session_id>/add/<int:person_id>/', views.register, name='register_person'),
    path('sessions/<int:session_id>/remove/<int:person_id>/', views.remove_person, name='remove_person'),
    path('sessions/<int:pk>/classlist/', views.AttendanceView.as_view(), name='attendance'),
    path('sessions/<int:event_id>/edit/classes/add/<int:class_id>', views.add_class_event, name='add_class_event'),
    path('sessions/<int:event_id>/edit/classes/remove/<session_id>', views.remove_class, name='remove_class')
]


