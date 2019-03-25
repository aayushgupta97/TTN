from django import template

register = template.Library()
custom_data = [num for num in range(0,1000)]

@register.simple_tag
def custom_tag():
	return len(custom_data)


@register.filter
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()