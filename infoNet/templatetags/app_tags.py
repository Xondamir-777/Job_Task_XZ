from django import template
from infoNet.models import *
from infoNet.Menu_dict import get_menu

register = template.Library()

@register.simple_tag()
def get_menu():
#     menu = {"Markaz": {"data_menu_id": "rc-menu-uuid-36672-1-about", 'url':{'exist': True,'src':'info', 'val': 'AboutCenter'}},
# "Resurslar": {"data_menu_id":"rc-menu-uuid-36672-1-service", 'url':{'exist': True,'src':'src', 'val': 'service'}},
# "Loyihalar": {"data_menu_id":"rc-menu-uuid-36672-1-project", 'url':{'exist': True,'src':'project0', 'val': None}},
# "Nashrlar": {"data_menu_id":"rc-menu-uuid-36672-1-Publication", 'url':{'exist': True,'src':'publication', 'val': None}},
# "Hamkorlik": {"data_menu_id":"rc-menu-uuid-36672-1-engagement", 'url':{'exist': True,'src':"partners", 'val': None}},
# "Yangiliklar": {"data_menu_id":"rc-menu-uuid-36672-1-new", 'url':{'exist': True,'src':"allNews", 'val': None}},
# "Ochiq ma'lumotlar": {"data_menu_id":"rc-menu-uuid-36672-1-openData", 'url':{'exist': True,'src':"public_info", 'val': None}},
# "Biz bilan bog‘lanish": {"data_menu_id":"rc-menu-uuid-36672-1-contact", 'url':{'exist': True,'src':'contact', 'val': None}}}

    return get_menu()

@register.simple_tag()
def get_contact_info():
    contact_info = {
            "Email":{"txt": "info.csti@ilmiy.uz", 'type':'email', 'link':"info.csti@ilmiy.uz"},
            "Telefon":{"txt": "+998 (71) 203-32-23", 'type':'tel', 'link':'998712033223'},
            "Manzil": {"txt": "100174, Toshkent sh., Olmazor tumani., Universitet ko‘chasi., 7-uy", 'type':None, 'link':None}
        }
    return contact_info
@register.inclusion_tag('tags/linkget.html')
def check_link(element, text, arg=None):
    return {'el':element, 'text': text, 'arg': arg}


# "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3  gap-6"
@register.inclusion_tag('tags/post.html')
def show_simple_post(element, post_style, posts_photos=None):
    return {'el': element, 'style':post_style, 'photos':posts_photos}

@register.inclusion_tag('tags/Grid_show_list.html')
def show_simple_grid_post(element, post_style, page_content, grid_style):
    return {'el': element, 
            'post_style':post_style, 
            "content": page_content, 
            'grid_style':grid_style}


@register.inclusion_tag('tags/picture_changer.html')
def change_photo(photo):
    return {'photos': photo}



# @register.filter
# def mul(value, arg):
#     return value * arg

@register.filter
def div(value, arg):
    return int(value / arg) + int(value%arg>0)



@register.simple_tag
def url_replace(request, **kwargs):

    query = request.GET.copy()

    for k, v in kwargs.items():
        query[k] = v

    return query.urlencode()

# ?page={{ page_obj.next_page_number }}&page_size={{ page_obj.paginator.per_page }}&title_serch={{ request.GET.title_serch }}&data_serch={{ request.GET.data_serch }}
# ?page={{ p }}&page_size={{ page_obj.paginator.per_page }}&title_serch={{ request.GET.title_serch }}&data_serch={{ request.GET.data_serch }}
# ?page={{ page_obj.previous_page_number }}&page_size={{ page_obj.paginator.per_page }}&title_serch={{ request.GET.title_serch }}&data_serch={{ request.GET.data_serch }}

# {{ request.path }}?page_size={{ i }}&page=&title_serch={{ request.GET.title_serch }}&data_serch={{ request.GET.data_serch }}


@register.inclusion_tag('tags/paginate.html')
def paginate_tag(request, paginator, page_obj, numbers):
    return {'request': request, 'paginator':paginator, 'page_obj':page_obj, 'numbers':numbers}