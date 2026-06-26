from .models import Projects, Publication, VideoType
from django.utils.translation import gettext as _

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

