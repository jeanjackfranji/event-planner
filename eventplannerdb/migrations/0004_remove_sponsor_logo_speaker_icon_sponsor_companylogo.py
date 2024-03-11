# Generated by Django 4.2.11 on 2024-03-11 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventplannerdb", "0003_speaker_contactnumber_speaker_email_sponsor_website"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sponsor",
            name="logo",
        ),
        migrations.AddField(
            model_name="speaker",
            name="icon",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="sponsor",
            name="companyLogo",
            field=models.CharField(default="", max_length=255),
        ),
    ]