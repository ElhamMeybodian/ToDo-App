from django import template

register = template.Library()


@register.filter()
def capital_title(arg):
    return arg[0].capitalize() + arg[1:]
