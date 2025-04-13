from django.contrib import admin

from mtm.models import Publication,Article
# Register your models here.

# @admin.register(Article)
class Article_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Article._meta.fields]                  #SHOW ALL FILDES
        list_display=all_fields
        readonly_fields=('id',)

class Publication_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Publication._meta.fields]                #SHOW ALL FILDES
        list_display=all_fields
 
                   
admin.site.register(Publication,Publication_Admin)
admin.site.register(Article,Article_Admin)
