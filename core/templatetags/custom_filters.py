from django import template

register = template.Library()

@register.filter(name='split')
def split_filter(value, delimiter=','):
    """Split a string by delimiter"""
    return value.split(delimiter)

@register.filter(name='get_item')
def get_item(lst, index):
    try:
        return lst[index]
    except (IndexError, TypeError):
        return ''
