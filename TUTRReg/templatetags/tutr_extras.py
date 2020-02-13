from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group_name = group_name.split(', ')
    for group in group_name:
        if user.groups.filter(name=group).exists():
            return True
    return False
