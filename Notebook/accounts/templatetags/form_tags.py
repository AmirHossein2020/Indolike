from django import template

register = template.Library()
# This filter adds a CSS class to a form field for styling purposes.
@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})
