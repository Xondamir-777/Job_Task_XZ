
from .models import *


class PublicationsViewBase():
    # template_name = 'grid_show.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nashrlar'
        context['style'] = 'publisher'

        context['nav_style'] = "w-full static  backdrop-blur-md px-2 md:px-0 transition-all duration-500 ease-in-out "
        context['side_list'] = {'Nashrlar': {'Nashrlar':{"sub_topic":[], "url": {'exist': True,'src':'publication', 'val': None}}}}

        for el in Publication.objects.all():
            print(el.title)
            context['side_list']['Nashrlar'][str(el.title)] = {"sub_topic":[
                {'name': "Jurnal soni", "url": {'exist': True,'src':'magazines', 'val': int(el.pk)}},
                {'name': "Tahririyat Kengashi", "url": {'exist': True,'src':'info', 'val': f"editorialBoard_{el.pk}" }},
                {'name': "Umumiy ma'lumotlar", "url": {'exist': True,'src':'info', 'val': f"overall_{el.pk}"}},
            ], "url": {'exist': False,'src':'', 'val': None}}
        
        # print(context['side_list'])
        return context
    

