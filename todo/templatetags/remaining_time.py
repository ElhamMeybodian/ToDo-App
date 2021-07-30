from django import template
from django.utils import timezone

register = template.Library()


@register.simple_tag
def my_tag(expired):
    return expired - timezone.now()
