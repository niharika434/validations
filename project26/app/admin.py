from django.contrib import admin

# Register your models here.
from app.models import*

class customizewebpage(admin.ModelAdmin):
    list_display=['topic_name','name','email','url']
    list_display_links=['url','email']
    search_fields=['name']
    list_editable=('name',)
    list_filter=['name','topic_name']
    list_per_page= 2
    #list_max_show_all= 3
    #list_select_related= ['topic_name']


admin.site.register(Topic)
admin.site.register(Webpage,customizewebpage)
admin.site.register(Accessrecord)