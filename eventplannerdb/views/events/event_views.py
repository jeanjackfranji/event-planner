from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...models import Event, Survey, Speaker, Agenda
from ...forms import SurveyForm


class EventListView(ListView):
    """
    Display an Event List View (showing all events and get method to filter on event name)
    """

    model = Event
    template_name = "event_list.html"
    context_object_name = "events"

    def get(self, request, *args, **kwargs):
        """
        Get the queryset based on the search input.
        """
        # Get Query search from search input
        query = request.GET.get("searchInput", "")
        # Filter on Events
        if query:
            self.queryset = Event.objects.filter(title__icontains=query)
        else:
            self.queryset = Event.objects.all()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Add the search query to the context data.
        """
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("searchInput", "")
        return context


class EventDetailView(DetailView):
    """
    Display an Event Detail View (showing more information on the event object)
    """

    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"


@login_required  # Ensure the user is logged in to register
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.user not in event.registered_users.all():
        event.registered_users.add(request.user)
        event.save()
        messages.success(request, "You have successfully registered for this event.")
    else:
        messages.error(request, "Registration failed. You are already registered for this event.")

    return redirect("event_detail", pk=event_id)


@login_required
def deregister_from_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.user in event.registered_users.all():
        event.registered_users.remove(request.user)
        event.save()
        messages.success(request, "You have successfully de-registered from this event.")
    else:
        messages.error(request, "De-Registration failed. You are already not registered for this event.")

    if request.user in event.checkedIn_users.all():
        event.checkedIn_users.remove(request.user)
        event.save()

    return redirect("event_detail", pk=event_id)


@login_required
def check_in_to_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.user not in event.checkedIn_users.all():
        event.checkedIn_users.add(request.user)
        event.save()
        messages.success(request, "You have successfully checked-in to this event.")
    else:
        messages.error(request, "check-in failed. You are already checked-in to this event.")

    return redirect("event_detail", pk=event_id)


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
    model = Agenda
    fields = ["event", "title", "start_time", "end_time"]
    template_name = "eventagenda_form.html"
    success_url = "/events/"  # Redirect to the event list after agenda creation
