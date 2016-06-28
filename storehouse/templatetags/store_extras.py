from django import template
from storehouse.models import Ware

register = template.Library()


@register.inclusion_tag('storehouse/wares.html')
def get_category_list():
    return {'waresnew': Ware.objects.all()}
