from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Event, Survey, EventAgenda, UserCheckIn
from .forms import SurveyForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class EventListView(ListView):
    model = Event
    template_name = "event_list.html"
    context_object_name = "events"

    def get(self, request):
        # Get Query search from search input
        query = request.GET.get("searchInput")
        # Filter on Events
        if query:
            events = Event.objects.filter(title__icontains=query)
        else:
            events = Event.objects.all()
            query = "" # empty query if no search input is given
        # Render needed Data and View
        return render(request, "event_list.html", {"events": events, "query": query})


class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"


class SurveyCreateView(CreateView):
    model = Survey
    form_class = SurveyForm
    template_name = "survey_form.html"
    success_url = "/events/"  # Redirect to the event list after survey creation


class EventAgendaCreateView(CreateView):
    model = EventAgenda
    fields = ["event", "title", "start_time", "end_time"]
    template_name = "eventagenda_form.html"
    success_url = "/events/"  # Redirect to the event list after agenda creation


class UserCheckInView(CreateView):
    model = UserCheckIn
    fields = ["user", "event"]
    template_name = "usercheckin_form.html"
    success_url = "/events/"  # Redirect to the event list after check-in


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("event_list")
        return render(request, "login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("event_list")
        return render(request, "signup.html", {"form": form})
