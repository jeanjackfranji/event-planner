# Generated by Django 4.2.11 on 2024-03-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventplannerdb", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="speaker",
            name="age",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]