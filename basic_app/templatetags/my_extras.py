from django import template

# register = template.Library()

@register.filter(name='cut') # this is a decorator
def filter_cut(value, arg):
  """
    This cuts out all values of "arg" from the string
  """
  return value.replace(arg, '')

# register.filter('cut', filter_cut)
