from django import template
from hello.models import Accounts

register = template.Library()

@register.simple_tag
def idToUsername(id):
    return Accounts.objects.get(pk=id).user.username