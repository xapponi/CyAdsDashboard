from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False

@register.filter(name='get_groups')
def has_group(user):
    group_list = []
    for group in user.groups.all():
        group_list.append(group.name)
    return group_list
    # return ["group1", "group2"]
