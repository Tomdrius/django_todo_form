from django import template
from bootstrap_datepicker_plus import DatePickerInput

register = template.Library()

@register.inclusion_tag('bootstrap_datepicker_plus_js.html')
def bootstrap_datepicker_plus_js():
    return {'media': DatePickerInput().media}

# from django import template

# def include_bootstrap_datepicker_plus_js(parser, token):
#     """
#     Include the JavaScript files for bootstrap-datepicker-plus.
#     """
#     nodelist = parser.parse(('endtag', 'bootstrap_datepicker_plus_js'))
#     parser.delete_first_token()
#     return nodelist