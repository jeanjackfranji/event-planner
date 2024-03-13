from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from eventplannerdb.views.events.event_views import Event


class EventListViewTest(TestCase):
    def setUp(self):
        self.url = reverse("event_list")

    def test_event_list_view_with_no_events(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["events"], [])

    def test_event_list_view_with_events(self):
        event = Event.objects.create(
            title="Test Event",
            location="Test Location",
            startDateTime="2024-05-20T13:00:00Z",
            endDateTime="2024-05-20T19:00:00Z",
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Event")

    def test_event_list_view_with_search_query(self):
        event = Event.objects.create(
            title="Test Event 2",
            location="Test Location",
            startDateTime="2024-05-20T13:00:00Z",
            endDateTime="2024-05-20T19:00:00Z",
        )
        response = self.client.get(self.url, {"searchInput": "Test"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test")


class EventDetailViewTest(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title="Test Event 3",
            location="Test Location",
            startDateTime="2024-05-20T13:00:00Z",
            endDateTime="2024-05-20T19:00:00Z",
        )
        self.url = reverse("event_detail", args=[self.event.pk])

    def test_event_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Event 3")


class RegisterForEventViewTest(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title="Test Event",
            location="Test Location",
            startDateTime="2024-05-20T13:00:00Z",
            endDateTime="2024-05-20T19:00:00Z",
        )
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.url = reverse("register_for_event", args=[self.event.pk])

    def test_register_for_event_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Should redirect after registration

        # Check if the user is registered for the event
        self.assertTrue(self.user in self.event.registered_users.all())


class CheckInForEventViewTest(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title="Test Event",
            location="Test Location",
            startDateTime="2024-05-20T13:00:00Z",
            endDateTime="2024-05-20T19:00:00Z",
        )
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.event.registered_users.add(self.user)
        self.url = reverse("check_in_to_event", args=[self.event.pk])

    def test_checkin_to_event_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Should redirect after checkin

        # Check if the user is checked in to the event
        self.assertTrue(self.user in self.event.checkedIn_users.all())


class DeRegisterFromEventViewTest(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title="Test Event",
            location="Test Location",
            startDateTime="2024-05-20T13:00:00Z",
            endDateTime="2024-05-20T19:00:00Z",
        )
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.event.registered_users.add(self.user)
        self.url = reverse("deregister_from_event", args=[self.event.pk])

    def test_deregister_from_event_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Should redirect after de-registration

        # Check if the user is de-registered for the event
        self.assertTrue(self.user not in self.event.registered_users.all())
