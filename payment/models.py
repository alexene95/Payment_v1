from django.db import models
#from django.utils import timezone 
from django.contrib.auth.models import User


# Create your models here.
# import datetime 
# d1=datetime.datetime.now()


class Pay (models.Model):
    CreditCardNumber=models.CharField(max_length=16)
    CardHolder=models.CharField(max_length=100)
    ExpirationDate=models.DateField()
    SecurityCode=models.IntegerField(blank=True,null=True)
    Amount=models.DecimalField( decimal_places=2 , max_digits=10000)
    
# -CreditCardNumber (mandatory, string, it should be a valid credit card number)
# - CardHolder: (mandatory, string)
# - ExpirationDate (mandatory, DateTime, it cannot be in the past)
# - SecurityCode (optional, string, 3 digits)
# - Amount (mandatoy decimal, positive amount)

    def ProcessPayment(self):
        try:
            float(Payment) >= 0
            return True
        except ValueError:
            return False
            
        today=date.today()
        
        try :
            ExpirationDate > today
            return True
        except ValueError:
            return False
            
        try: 
            len(CreditCardNumber)== 16
            return True
        except  ValueError:
            return False
            
            
            
            
            
            


