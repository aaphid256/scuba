# custom_filters.py in dives/templatetags/
from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def total_dive_time(dives):
    total_time = sum(dive.duration.total_seconds() for dive in dives)
    hours, remainder = divmod(total_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))