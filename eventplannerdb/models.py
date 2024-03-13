from django.db import models
from django.contrib.auth.models import User

CHOICES = [
    (1, "Not Satisfied"),
    (2, "Somewhat Satisfied"),
    (3, "Neutral"),
    (4, "Satisfied"),
    (5, "Very Satisfied"),
]


class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    description = models.TextField(default="")
    speakers = models.ManyToManyField("Speaker", related_name="events")
    sponsors = models.ManyToManyField("Sponsor", related_name="events")
    registered_users = models.ManyToManyField(User, related_name="registered_events", blank=True)
    checkedIn_users = models.ManyToManyField(User, through="CheckIn",
                                              related_name="checkedIn_events", blank=True)


class CheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    checkin_time = models.DateTimeField(auto_now_add=True)


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


class Agenda(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="agenda")
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Survey(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="surveys")
    title = models.CharField(max_length=255, default="")
    methodology = models.TextField(default="")
    is_anonymous = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions")
    question = models.CharField(max_length=500, default="")
    CHOICES = CHOICES


class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey_question = models.ForeignKey("SurveyQuestion", on_delete=models.CASCADE)
    response = models.IntegerField(choices=CHOICES)
