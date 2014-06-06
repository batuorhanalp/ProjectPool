from django import template
from ..models import Brand, Category, Budget
register = template.Library()


@register.assignment_tag(takes_context=False)
def get_brands():
    return Brand.objects


@register.assignment_tag(takes_context=False)
def get_categories():
    return Category.objects


@register.assignment_tag(takes_context=False)
def get_budgets():
    return Budget.objects


@register.filter
def default_if_none_or_empty(value, default_value):
    if not value or '' == value:
        return default_value
    else:
        return value