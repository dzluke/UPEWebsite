from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.core.exceptions import ValidationError
from django import forms
from django.forms import widgets

TYPE_CHOICES = (
    ('General','General'),
    ('Publicity', 'Publicity'),
    ('Social','Social'),
    ('Technical','Technical'),
    ('Infosession','Infosession'),
    ('Workshop','Workshop'),
)

TYPE_COLORS = {"General":"DarkBlue", "Publicity":"Crimson", "Social":"ForestGreen",
                "Technical":"Indigo", "Infosession":"LightSeaGreen", "Workshop":"Orange"}

class Event(models.Model):
    name = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=10000, choices=TYPE_CHOICES, default='General')
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField('Start Time', help_text=u'Start time')
    #start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s" style="color: %s" > <font size = 1>%s </font> %s</a>' % (url, TYPE_COLORS[str(self.type)], self.start_time.strftime("%I:%M %p"), str(self.name)) #This is where you put the name

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')


# Create your models here.
