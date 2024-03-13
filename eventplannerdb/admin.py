from django.contrib import admin
from .models import Event, Speaker, Sponsor, Survey, EventAgenda

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Survey)
admin.site.register(EventAgenda)
