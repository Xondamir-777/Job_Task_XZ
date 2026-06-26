from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
@register(VideoNews)
class VideoNewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
@register(Leadership)
class LeadershipTranslationOptions(TranslationOptions):
    fields = ('name', 'position')
@register(Vacancies)
class VacanciesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'editorial_board', 'general_information')
@register(Partners)
class PartnersTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
@register(InfoSySsrc)
class InfoSySsrcTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

    
@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')