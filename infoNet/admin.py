from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(News)
admin.site.register(VideoNews)
admin.site.register(Publication)
admin.site.register(MagazinesPDF)
admin.site.register(Projects)
admin.site.register(Partners)
admin.site.register(Brochures)
admin.site.register(UsersMessage)
admin.site.register(Leadership)
admin.site.register(AboutUs)
admin.site.register(InfoSySsrc)


class PhotostInline(admin.TabularInline):
    model = NewsPhotos
    extra = 1


@admin.register(News)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [PhotostInline]