from django.contrib import admin

from otm.models import Reporter,Article
# Register your models here.

# @admin.register(Reporter)
class Reporter_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Reporter._meta.fields]                  #SHOW ALL FILDES
        list_display=all_fields
        readonly_fields=('id',)

class Article_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Article._meta.fields]                #SHOW ALL FILDES
        list_display=all_fields
        
admin.site.register(Reporter,Reporter_Admin)
admin.site.register(Article,Article_Admin)
