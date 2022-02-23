from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def replace_commas(string):
    return string.replace(',', '.')


@register.filter
def to_str(value):
    return str(value)


