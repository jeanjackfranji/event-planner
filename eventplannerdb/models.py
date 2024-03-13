from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    description = models.TextField(default="")
    speakers = models.ManyToManyField("Speaker", related_name="events")
    sponsors = models.ManyToManyField("Sponsor", related_name="events")
    registered_users = models.ManyToManyField(User, related_name="registered_events", blank=True)
    checkedIn_users = models.ManyToManyField(User, related_name="checkedIn_events", blank=True)


class Speaker(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)
    contactNumber = models.CharField(max_length=255, default="")
    email = models.EmailField(default="")
    bio = models.TextField()
    icon = models.CharField(max_length=255, default="")


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(default="")
    companyLogo = models.CharField(max_length=255, default="")


class Survey(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    CHOICES = [
        (1, "Not Satisfied"),
        (2, "Somewhat Satisfied"),
        (3, "Neutral"),
        (4, "Satisfied"),
        (5, "Very Satisfied"),
    ]
    user_response = models.IntegerField(choices=CHOICES)


class EventAgenda(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
