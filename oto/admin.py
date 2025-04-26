from django.contrib import admin

# Register your models here.
from oto.models import Place,Restaurant,Waiter
# Register your models here.

# # @admin.register(Place)
# class Place_Admin(admin.ModelAdmin):
#         all_fields = [f.name for f in Place._meta.fields]+["id"]                  #SHOW ALL FILDES
#         list_display=all_fields
#         readonly_fields=('id',)

# class Restaurant_Admin(admin.ModelAdmin):
#         all_fields = ["pk"]+[f.name for f in Restaurant._meta.fields]                #SHOW ALL FILDES
#         list_display=all_fields

# class Waiter_Admin(admin.ModelAdmin):
#         all_fields = [f.name for f in Waiter._meta.fields]+["id"]                  #SHOW ALL FILDES
#         list_display=all_fields     
                   
# admin.site.register(Place,Place_Admin)
# admin.site.register(Restaurant,Restaurant_Admin)
# admin.site.register(Waiter,Waiter_Admin)