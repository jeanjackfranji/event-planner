from django.contrib import admin
from .models import Event, Speaker, Sponsor, Survey, SurveyQuestion, SurveyResponse, Agenda

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Agenda)
admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyResponse)
