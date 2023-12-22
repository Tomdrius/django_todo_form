from django import template
from bootstrap_datepicker_plus import DatePickerInput

register = template.Library()

@register.inclusion_tag('bootstrap_datepicker_plus_js.html')
def bootstrap_datepicker_plus_js():
    return {'media': DatePickerInput().media}