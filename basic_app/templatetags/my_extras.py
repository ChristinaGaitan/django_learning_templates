from django import template

register = template.Library()

def filter_cut(value, arg):
  """
    This cuts out all values of "arg" from the string
  """
  return value.replace(arg, '')

register.filter('cut', filter_cut)
