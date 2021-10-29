from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg,'') #replace arg with '' (remove arg)

# register.filter('cut',cut)          #this registers the cut function with the name 'cut'
