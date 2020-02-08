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
    path('faq/', TemplateView.as_view(template_name='TUTRReg/faq.html'), name='faq'),
    path('documents/', TemplateView.as_view(template_name='TUTRReg/docs.html'), name='documents'),
    path('links/', TemplateView.as_view(template_name='TUTRReg/links.html'), name='links'),
    path('sessions/', views.SessionView.as_view(), name='sessions'),
    path('sessions/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
    path('sessions/<int:session_id>/<int:pk>', views.EventClassDetail.as_view(), name='event_class_detail'),
    path('classes/<int:pk>', views.ClassDetail.as_view(), name='class_detail'),
    path('courses/<int:pk>', views.CourseDetail.as_view(), name='course_detail'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='TUTRReg/login.html')),
    path('landing/', views.LandingView.as_view(), name='landing'),
    path('sessions/<int:session_id>/<int:class_id>/register/', views.register, name='register'),
    path('sessions/new', views.new_event, name='new_event')
]


