# Generated by Django 4.2.11 on 2024-03-11 16:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("eventplannerdb", "0005_event_registered_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="checkedIn_users",
            field=models.ManyToManyField(blank=True, related_name="checkedIn_events", to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name="UserCheckIn",
        ),
    ]
