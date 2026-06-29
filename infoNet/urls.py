
from django.urls import path, include
from .views import *

from django.conf.urls.i18n import set_language
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60*10)(index.as_view()), name='home'),
    path('new/<int:id>/', New.as_view(), name='new'),
    path('new/video/<slug:type>/', cache_page(60*10)(ShowVideo.as_view()), name='videoNews'),
    path('new/news/', allNews.as_view(), name='allNews'),
    path('new/Brouchers/', ShowBrouchers.as_view(), name='ShowBrouchersNews'),
    path('publication/', cache_page(60*10)(PublicationsView.as_view()), name='publication'),
    path('engagement/collaborations', cache_page(60*10)(ourPartners.as_view()), name='partners'), 
    path('engagement/collaborations/<int:id>', partnerID.as_view(), name='partnerID'), 
    path('publication/<int:id>/', Magazines.as_view(), name='magazines'), 
    path('info/<slug:info>/', cache_page(60*10)(ShowInfo.as_view()), name='info'),
    path('about_us/<slug:info>/', cache_page(60*10)(ShowInfoAboutUs.as_view()), name='aboutus'),
    path('public_info/', cache_page(60*10)(PublicInfo.as_view()), name='public_info'),
    path('project/', cache_page(60*10)(Project.as_view()), name='project0'),
    path('project/<int:id>/', cache_page(60*10)(Project.as_view()), name='project'),
    path('resurlar/', cache_page(60*10)(Sources.as_view()), name='src0'), 
    path('resurlar/<slug:page>', cache_page(60*10)(Sources.as_view()), name='src'), 
    # path('leaders/', Leaders.as_view(), name='leaders'),
    path('leaders/<slug:pos>/', cache_page(60*10)(Leaders.as_view()), name='leaders_pos'),
    path('vacancy/', Vacancy_list.as_view(), name='vacancy'),
    path('Contact/', Contacts.as_view(), name='contact'),
    path(
        "i18n/setlang/",
        set_language,
        name="set_language"
    ),
]