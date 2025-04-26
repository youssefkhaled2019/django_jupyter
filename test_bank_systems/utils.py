# from .models import BankAccount
from django.apps import apps
import random
import string

class Helper:
    @staticmethod
    def generate_account_number(prefex=None):
        model=apps.get_model("test_bank_systems","BankAccount")
        while True:
            account_number=''.join(random.choices(string.digits,k=12))
            if prefex is not None:
                account_number=f'{prefex}{account_number}'
            if not model.objects.filter(account_number=account_number).exists():
                return account_number

    @staticmethod
    def generate_transaction_number():
        model=apps.get_model("test_bank_systems","Transaction")
        while True:
            transaction_number=''.join(random.choices(string.digits,k=12))
            # if prefex is not None:
            #     transaction_number=f'{transaction_number}'
            if not model.objects.filter(transaction_number=transaction_number).exists():
                return transaction_number