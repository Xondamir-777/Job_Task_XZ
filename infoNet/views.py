from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, TemplateView
# from .Menu_dict import get_menu
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
class menu_url():
    def __init__(self, exist:bool, src:str, val=None):
        self.exist = exist
        self.src = src
        self.val = val

class Menu_element():
    def __init__(self, title, sub_topic:list , url:menu_url, data_menu_id = None):
        self.title = title
        self.url = url
        self.sub_topic = sub_topic
        self.data_menu_id = data_menu_id
def get_menu():
    print("LANG =", get_language())
    prj = list()
    for el in Projects.objects.all():
        prj.append(Menu_element(el.title, [], menu_url(True, 'project', int(el.pk))))
        
    publication = list() 
    publication.append(Menu_element(_('Nashrlar'), [], menu_url(True, 'publication')))
    for el in Publication.objects.all():
        print(el.title)
        publication.append(Menu_element(el.title, [
            Menu_element(_("Jurnal soni"), [], menu_url(True, 'magazines', int(el.pk))),
            Menu_element(_("Tahririyat Kengashi"), [], menu_url(True, 'info', f"editorialBoard_{el.pk}")),
            Menu_element(_("Umumiy ma'lumotlar"), [], menu_url(True, 'info', f"overall_{el.pk}")),
        ], menu_url(False, '', None)))

    videos=list()
    videos.append(Menu_element(_("So'ngi yangiliklar"), [], menu_url(True, 'allNews')))
            
    for key, val in VideoType.choices:
        videos.append(Menu_element(val, [], menu_url(True, 'videoNews', key)))

    videos.append(Menu_element('One-Page Brochure', [], menu_url(True, 'ShowBrouchersNews')))


    menu_n = {"Markaz": Menu_element(_("Markaz"), [
                            Menu_element(_("Markaz haqida"), [] , menu_url(True, 'aboutus', 'AboutCenter')),
                            Menu_element(_("Me’yoriy hujjatlar"), [] , menu_url(True, 'aboutus', 'AboutDocs')),
                            Menu_element(_("Rahbariyat"), [] , menu_url(True, 'leaders_pos', 'Leadership')),
                            Menu_element(_("Bo‘sh ish o‘rinlari"), [] , menu_url(True, 'vacancy')),
                    ], menu_url(True, 'aboutus', 'AboutCenter'), ["rc-menu-uuid-36672-","-about"]),
                    
            "Resurslar": Menu_element(_("Resurslar"), [
                            Menu_element(_("Axborot tizimlari"), [] , menu_url(True, 'src', 'service')),
                            Menu_element(_("Jurnallar"), [] , menu_url(True, 'src', 'subscription')),
                            Menu_element(_("Ma'lumotlarni tahlil qilish"), [] , menu_url(True, 'src', 'data-boards')),
                    ], menu_url(True, 'src', 'service'), ["rc-menu-uuid-36672-", "-service"]),

            "Loyihalar": Menu_element(_("Loyihalar"), prj, menu_url(True, 'project0'), ["rc-menu-uuid-36672-", "-project"]),

            "Nashrlar": Menu_element(_("Nashrlar"), publication, menu_url(True, 'publication'), ["rc-menu-uuid-36672-", "-Publication"]),

            "Hamkorlik": Menu_element(_("Hamkorlik"), [
                            Menu_element(_("Hamkorlar"), [] , menu_url(False, '', 'service')),
                    ], menu_url(True, 'partners'), ["rc-menu-uuid-36672-","-engagement"]),

            "Yangiliklar": Menu_element(_("Yangiliklar"), videos, menu_url(True, 'allNews'), ["rc-menu-uuid-36672-", "-new"]),

            "Ochiq ma'lumotlar": Menu_element(_("Ochiq ma'lumotlar"), [
                            Menu_element(_("Ochiq ma'lumotlar"), [] , menu_url(False, '')),
                    ], menu_url(True, 'public_info'), ["rc-menu-uuid-36672-","-openData"]),

            "Biz bilan bog‘lanish": Menu_element(_("Biz bilan bog‘lanish"), [
                            Menu_element(_("Biz bilan bog‘lanish"), [] , menu_url(False, '')),
                    ], menu_url(True, 'contact'), ["rc-menu-uuid-36672-","-contact"]),
    }
    return menu_n



class Base(ListView):
    
    menu = get_menu()
    context_object_name = 'content'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.menu
        context['numbers'] = [1, 2, 4, 16]
        context['lang'] = self.request.LANGUAGE_CODE
        return context

    
class index(Base):
    model = News
    template_name = 'index.html'
    # extra_context = {"nav_style": 'w-full fixed top-0 z-50  backdrop-blur-md px-2 md:px-0 transition-all duration-500 ease-in-out bg-transparent text-white',
    #                  "text_color": "white",}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blur'] = True
        context['one_page'] = Brochures.objects.order_by('-time_creation')[:4]
        context['content'] = News.objects.order_by('-time_creation')[:7]
        return context

    
   


class allNews(Base):
    model = News
    template_name = 'all_news.html'
    # paginate_by=3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('So‘nggi yangiliklar')
        context['style'] = 'news'
        context['side_list'] = context['menu']['Yangiliklar']

    
        # context[]
        return context
    def get_queryset(self):
        queryset = super().get_queryset()

        title = self.request.GET.get('title_serch')
        start_date = self.request.GET.get('start_date')
        finish_date = self.request.GET.get('finish_date')
        # el_count = self.request.GET.get('num')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if start_date:
            queryset = queryset.filter(time_creation__date__gte=start_date)

        if finish_date:
            queryset = queryset.filter(time_creation__date__lte=finish_date)
            
        print(start_date)
 
        return queryset
    def get_paginate_by(self, queryset):
        try:
            page_size = int(self.request.GET.get('page_size', 4))
        except ValueError:
            page_size = 4

        return page_size

class New(Base):
    model = News
    template_name = 'new.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['side_list'] = context['menu']['Yangiliklar']
        # context['back_button'] = True
        # context['back_link'] = 'allNews'
        context['right_side'] = News.objects.order_by('-time_creation')
        # context['photos'] = NewsPhotos.objects.filter(news_id=int(context['content'].pk))
        return context
    
    def get_queryset(self):
        query = super().get_queryset()
        # print(20*'-',self.kwargs['id'],20*'-')
        return query.get(pk=int(self.kwargs['id']))

class ShowVideo(Base):
    model = VideoNews
    template_name = "all_news.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['side_list'] = context['menu']['Yangiliklar'] 
        context['style'] = "video"
        context['title'] = dict(VideoType.choices).get(str(self.kwargs['type']))
        return context
    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('title_serch')
        queryset = queryset.filter(news_type=str(self.kwargs['type']))
        if query:
            queryset = queryset.filter(title__icontains=query)
            # print("--------------->"+str(VideoNews.choices[int(self.kwargs['type']-1)][0]))
        # else:
            
            # print("--------------->"+str(VideoNews.choices[int(self.kwargs['type']-1)][0]))

        return queryset
    def get_paginate_by(self, queryset):
        try:
            page_size = int(self.request.GET.get('page_size', 4))
        except ValueError:
            page_size = 4

        return page_size
    

class ShowBrouchers(Base):
    model = Brochures
    template_name = "grid_show.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['side_list'] = context['menu']['Yangiliklar'] 
        context['style'] = "Brochures"
        context['title'] = "One-Page Brochure"
        return context
    def get_paginate_by(self, queryset):
        try:
            page_size = int(self.request.GET.get('page_size', 4))
        except ValueError:
            page_size = 4

        return page_size



class ourPartners(Base):
    model = Partners
    template_name = 'column_show.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['menu']["Hamkorlik"]['url'] = 'partners'
        context['title'] = context['menu']['Hamkorlik'].title
        context['style'] = 'partners'

        context['side_list'] = context['menu']['Hamkorlik']
        return context

class partnerID(ourPartners):
    template_name = 'showInfoPage.html'
    
    extra_context = {'header': False, 'show_photo':False, 'back_button':False}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_photo'] = True
        # context['photo'] = pub.photo
        context['back_button'] = True
        context['back_link'] = 'partners'
        context['header'] = True
        # context['title'] = pub.title
        context['Text'] = context['content'].content
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.get(pk=int(self.kwargs['id']))

        return queryset




class PublicInfo(Base):
    template_name = 'public_info.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['side_list'] = context['menu']["Ochiq ma'lumotlar"]
    #     return context
    def get_queryset(self):
        return None


class Project(Base):

    model = Projects
    template_name = 'projects.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Loyihalar'

        context['side_list'] = context['menu']['Loyihalar']
        # {'Loyihalar':dict()}
        # for el in Projects.objects.all():
        #     context['side_list']['Loyihalar'][str(el.title)] = {"sub_topic":[], "url": {'exist': True,'src':'project', 'val': int(el.pk)}}
        
        # print(context['side_list'])
        return context
    def get_queryset(self):
        # context['title'] = 'Loyihalar'
        # res= None
        # if Projects.objects.all():
        res = Projects.objects.all().first()
        if self.kwargs.get('id'):
            # extra_context = {"title": res.title}
            res = Projects.objects.get(pk=int(self.kwargs['id']))
            # print(20*'-'+'>'+str(res))
            return res
        return res
        
class PublicationsView(Base):
    model = Publication
    template_name = 'column_show.html'
    # template_name = 'grid_show.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nashrlar'
        context['style'] = 'publisher'

        context['side_list'] = context['menu']['Nashrlar'] 
        return context



class Magazines(PublicationsView):
    model = MagazinesPDF
    template_name = 'magazines.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Jurnallar'
        # context['numbers'] = [1, 2, 4, 16]
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication=int(self.kwargs['id']))

        start_date = self.request.GET.get('start_date')
        finish_date = self.request.GET.get('finish_date')
        defined_date = self.request.GET.get('defined_date')

        if defined_date:
            queryset = queryset.filter(time_creation__date=start_date)
        else:
            if start_date:
                queryset = queryset.filter(time_creation__date__gte=start_date)

            if finish_date:
                queryset = queryset.filter(time_creation__date__lte=finish_date)
            
        # print(start_date)

        return queryset
    def get_paginate_by(self, queryset):
        try:
            page_size = int(self.request.GET.get('page_size', 4))
        except ValueError:
            page_size = 4

        return page_size


class ShowInfo(Base):
    model = Publication
    template_name = 'showInfoPage.html'
    extra_context = {'header': False, 'show_photo':False, 'back_button':False}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        arg = self.kwargs['info'].split('_')
        context['side_list'] = context['menu']['Nashrlar'] 
        # pub = Publication.objects.get(pk=int(arg[1]))
        if arg[0] == 'editorialBoard':
            context['show_photo'] = True
            # context['photo'] = context['content'].photo
            context['header'] = True
            # context['title'] = context['content'].title
            context['Text'] = context['content'].editorial_board

        elif arg[0] == 'overall':
            # pub = Publication.objects.get(pk=int(arg[1]))
            context['Text'] = context['content'].general_information

        # context['publication'] = pub

        return context
    def get_queryset(self):
        queryset= super().get_queryset()
        arg = self.kwargs['info'].split('_')
        queryset = queryset.get(pk=int(arg[1]))
        return queryset


class ShowInfoAboutUs(Base):
    model = AboutUs
    template_name = 'showInfoPage.html'
    extra_context = {'header': False, 'show_photo':False, 'back_button':False}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        # arg = self.kwargs['info'].split('_')
        context['side_list'] = context['menu']['Markaz']
        context['header'] = True
        # context['title'] = context['content'].title
        context['Text'] = context['content'].content
        # context['publication'] = pub
        return context
    
    def get_queryset(self):
        queryset= super().get_queryset()
        arg = self.kwargs['info']
        if arg == 'AboutCenter':
            queryset = queryset.get(pk=2)
            
        elif arg == 'AboutDocs':
            
            queryset = queryset.get(pk=1)
        # queryset = queryset.get(pk=int(arg[1]))
        return queryset




class Sources(Base):
    model = InfoSySsrc
    template_name = 'grid_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['menu']['Resurslar'].title
        context['style'] = 'post'
        context['side_list'] = context['menu']['Resurslar'] 
        return context
    def get_template_names(self):
        page = self.kwargs.get('page')

        if page in ['subscription', 'data-boards']:
            return ['column_show.html']

        return ['grid_show.html']

    def get_queryset(self):
        queryset= super().get_queryset()
        page = self.kwargs.get('page')

        if page == "service":
            return queryset.filter(type='Information System')

        elif page == "subscription":
            return Publication.objects.all()

        elif page == "data-boards":
            return queryset.filter(type='Data Analys')

        return queryset.none()
    # def get_paginate_by(self, queryset):
    #     try:
    #         page_size = int(self.request.GET.get('page_size', 4))
    #     except ValueError:
    #         page_size = 4

    #     return page_size


        
class Leaders(Base):
    model = Leadership
    template_name = 'Leaders.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['side_list'] = context['menu']['Markaz']
        context['right_side_list'] = positions.choices
        return context
    def get_queryset(self):
        queryset= super().get_queryset()
        arg= self.kwargs.get('pos')
        if arg:
            queryset = queryset.filter(structure=str(arg))
            # print(str(arg))

        return queryset



class Vacancy_list(Base):
    model = Vacancies
    template_name = 'column_show.html'
    extra_context = {'header': False, 'show_photo':False, 'back_button':False}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['side_list'] = context['menu']['Markaz'] 
        context['style'] = "post"
        context['title'] = "Bo‘sh ish o‘rinlari"
        return context



# class Contact(Base):
#     model = UsersMessage
    
#     template_name = "Contact.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)  
#         context['side_list'] = {"Biz bilan bog‘lanish": {"Biz bilan bog‘lanish": {"sub_topics":[], "url": {'exist': False,'src':'', 'val': None}}}}
#         context['title'] = "One-Page Brochure"
#         return context

class Contacts(TemplateView):
    menu = get_menu()   
    template_name = 'Contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['menu'] = self.menu
        # context['side_list'] = {"Biz bilan bog‘lanish": {"Biz bilan bog‘lanish": {"sub_topics":[], "url": {'exist': False,'src':'', 'val': None}}}}
        # context['title'] = "Biz bilan bog‘lanish"
        context['side_list'] = self.menu['Biz bilan bog‘lanish'] 
        context['error']=False

        return context

    def post(self, request, *args, **kwargs):

        full_name = request.POST.get('full_name')

        email = request.POST.get('email')

        phone = request.POST.get('phone')

        message = request.POST.get('message')
        if (full_name != '' and email != '' and phone != '' and message != ''):
            print(full_name, email, phone, message)
            UsersMessage.objects.create(
                user_name=request.POST.get('full_name'),
                user_email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                message=request.POST.get('message')
            )
            return redirect('contact')
        
        print("error")
        context = self.get_context_data()
        context['error']=True
        return self.render_to_response(
            context
        )


