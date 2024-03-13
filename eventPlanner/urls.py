"""
URL configuration for eventPlanner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from eventplannerdb.views import (
    EventListView,
    EventDetailView,
    SpeakerDetailView,
    SurveyCreateView,
    EventAgendaCreateView,
    LoginView,
    LogoutView,
    SignupView,
    register_for_event,
    deregister_from_event,
    check_in_to_event
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("events/", EventListView.as_view(), name="event_list"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path('events/<int:event_id>/register/', register_for_event, name='register_for_event'),
    path('events/<int:event_id>/deregister/', deregister_from_event, name='deregister_from_event'),
    path('events/<int:event_id>/checkin/', check_in_to_event, name='check_in_to_event'),
    path("speaker/<int:pk>/", SpeakerDetailView.as_view(), name="speaker_detail"),
    path("survey/create/", SurveyCreateView.as_view(), name="survey_create"),
    path("agenda/create/", EventAgendaCreateView.as_view(), name="agenda_create"),
    path("", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
]
