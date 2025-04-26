from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Transaction
@receiver(post_save, sender=Transaction)
def transaction_signals(sender, instance, created, **kwargs):
    if created:
       print("sssss")
       account=instance.account
       if(instance.transaction_type == "WD"):
            account.balance-=instance.amount
       elif(instance.transaction_type == "DP"):
            account.balance+=instance.amount
       account.save()
# print(instance.transaction_type  == Transaction.TransactionType.DEPOSIT)#true
