
from django.urls import path, include
from .views import *

from django.conf.urls.i18n import set_language
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', index.as_view(), name='home'),
    path('new/<int:id>/', New.as_view(), name='new'),
    path('new/video/<slug:type>/',ShowVideo.as_view(), name='videoNews'),
    path('new/news/', allNews.as_view(), name='allNews'),
    path('new/Brouchers/', ShowBrouchers.as_view(), name='ShowBrouchersNews'),
    path('publication/',PublicationsView.as_view(), name='publication'),
    path('engagement/collaborations', ourPartners.as_view(), name='partners'), 
    path('engagement/collaborations/<int:id>', partnerID.as_view(), name='partnerID'), 
    path('publication/<int:id>/', Magazines.as_view(), name='magazines'), 
    path('info/<slug:info>/', ShowInfo.as_view(), name='info'),
    path('about_us/<slug:info>/', ShowInfoAboutUs.as_view(), name='aboutus'),
    path('public_info/', PublicInfo.as_view(), name='public_info'),
    path('project/', Project.as_view(), name='project0'),
    path('project/<int:id>/', Project.as_view(), name='project'),
    path('resurlar/', Sources.as_view(), name='src0'), 
    path('resurlar/<slug:page>', Sources.as_view(), name='src'), 
    # path('leaders/', Leaders.as_view(), name='leaders'),
    path('leaders/<slug:pos>/', Leaders.as_view(), name='leaders_pos'),
    path('vacancy/', Vacancy_list.as_view(), name='vacancy'),
    path('Contact/', Contacts.as_view(), name='contact'),
    path(
        "i18n/setlang/",
        set_language,
        name="set_language"
    ),
]