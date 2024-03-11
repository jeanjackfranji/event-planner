from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Event, Survey, Speaker, EventAgenda
from .forms import SurveyForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
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

@login_required  # Ensure the user is logged in to register
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.user not in event.registered_users.all():
        event.registered_users.add(request.user)
        event.save()

    return redirect('event_detail', pk=event_id)

@login_required
def deregister_from_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.user in event.registered_users.all():
        event.registered_users.remove(request.user)
    
    if request.user in event.checkedIn_users.all():
        event.checkedIn_users.remove(request.user)
    
    event.save()
    
    return redirect('event_detail', pk=event_id)

@login_required
def check_in_to_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.user not in event.checkedIn_users.all():
        event.checkedIn_users.add(request.user)
        event.save()
    
    return redirect('event_detail', pk=event_id)

class SpeakerDetailView(DetailView):
    model = Speaker
    template_name = "speaker_detail.html"
    context_object_name = "speaker"

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
