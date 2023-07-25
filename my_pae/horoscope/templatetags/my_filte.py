from django import template
# stringfilter будут гарантировать что значение value будет принимать строку
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter(name='split')
@stringfilter
def split(value, key=' '):
    return value.split(key)
