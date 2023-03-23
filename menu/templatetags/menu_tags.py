from django import template
from django.urls import reverse

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    item_counter = 0
    active_item_counter = -1

    menu_items = MenuItem.objects.select_related('menu').filter(menu__slug=menu_name).select_related('parent')
    menu_url = reverse('menu', kwargs={'menu_name': menu_name})
    current_url = context.request.path

    active_menu = current_url == menu_url or current_url.startswith(menu_url)

    def build_tree(parent):
        nonlocal item_counter, active_item_counter

        menu_dict = {}
        childs = [item for item in menu_items if item.parent == parent]

        parent.counter = item_counter
        if parent.get_absolute_url() == current_url:
            parent.is_active = True
            active_item_counter = parent.counter
        item_counter += 1

        if not childs:
            menu_dict = {'item': parent, 'childs': {}}
            return menu_dict

        for child in childs:
            menu_dict[child.pk] = build_tree(child)
        return {'item': parent, 'childs': menu_dict}

    menu_dict = {}
    for item in menu_items:
        if item.parent is None:
            menu_dict[item.pk] = build_tree(item)

    return {'menu': menu_items[0].menu,
            'active_menu': active_menu,
            'menu_items': menu_dict,
            'active_item': active_item_counter,
            }
