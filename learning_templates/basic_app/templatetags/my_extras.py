from django import template

@register.filter(name='cut')

register= template.Library()

def cut(value,arg):
    """
    this cuts out all values og "arg" from the string
    """
    return value.replace(arg,'')

#register.filter('cut',cut)