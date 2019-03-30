from django import template
register = template.Library()

@register.filter
def format_date(date):
    return date.strftime('%Y/%m/%d')
