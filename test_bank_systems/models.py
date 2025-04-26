from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .utils import Helper 
from django.http import response


from django.http import Http404,JsonResponse
from django.shortcuts import get_object_or_404 as _get_object_or_404
class BankAccount(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="bankaccount")
    account_number=models.CharField(max_length=20,unique=True)#blank=True
    balance=models.DecimalField(max_digits=10,decimal_places=2,default=0.0,validators=[MinValueValidator(0.0)])#db_index=True
    created_at=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    # ddd=models.URLField()


    def __str__(self):
        return f'{self.user.username}-{self.account_number}'
    def save(self, *args, **kwargs):
        if  not self.account_number:
            self.account_number=Helper.generate_account_number("EG")
        return super().save(*args, **kwargs)
    
    class Meta:
        db_table ='BankAccount'
        constraints =[  models.CheckConstraint(check=models.Q(balance__gte=0), name="check_balance"),]
        indexes = [
            models.Index(fields=["balance"]), #https://docs.djangoproject.com/en/5.1/ref/models/options/#indexes
     
        ]


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        DEPOSIT='DP','Deposit'
        WITHDRAWAL='WD','Withdrawal'

    transaction_number=models.CharField(max_length=20,unique=True)#blank=True
    transaction_type=models.CharField(max_length=5,choices=TransactionType.choices)
    account=models.ForeignKey(BankAccount,on_delete=models.CASCADE,related_name="transactions")
    amount=models.DecimalField(max_digits=10,decimal_places=2)#db_index=True
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.transaction_type}-{self.transaction_number}'
    def clean(self):#validators
        print(self.transaction_type)

        try:
            if(self.amount<=0):
                raise ValidationError("amount woring")
            if(self.transaction_type == "WD"  and self.amount> self.account.balance):
                raise ValidationError("balance not enought")
        except ValidationError:
            #  raise ValidationError("balance not enought",status=204)
            raise Http404
        return super().clean()
    def save(self, *args, **kwargs):
        # self.clean()
        if  not self.transaction_number:
            self.transaction_number=Helper.generate_transaction_number()
        super().save( *args, **kwargs)
    
    class Meta:
        db_table ='Transaction'
        ordering=['-created_at']
        # constraints =[  models.CheckConstraint(check=models.Q(balance__gte=0), name="check_balance"),]
        # indexes = [
        #     models.Index(fields=["balance"]), #https://docs.djangoproject.com/en/5.1/ref/models/options/#indexes
        
        # ]