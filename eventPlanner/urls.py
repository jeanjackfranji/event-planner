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
    UserCheckInView,
    LoginView,
    LogoutView,
    SignupView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("events/", EventListView.as_view(), name="event_list"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("speaker/<int:pk>/", SpeakerDetailView.as_view(), name="speaker_detail"),
    path("survey/create/", SurveyCreateView.as_view(), name="survey_create"),
    path("agenda/create/", EventAgendaCreateView.as_view(), name="agenda_create"),
    path("checkin/create/", UserCheckInView.as_view(), name="checkin_create"),
    path("", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
]
