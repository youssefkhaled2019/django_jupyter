from django.contrib import admin
from.models import BankAccount,Transaction
# Register your models here.

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display=['id','user','account_number','balance','is_active','created_at']#
    readonly_fields=['account_number','balance']
    
    list_filter=['is_active']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin): 
    list_display=['id','account','transaction_number','transaction_type','amount','created_at']   
    readonly_fields=['transaction_number']