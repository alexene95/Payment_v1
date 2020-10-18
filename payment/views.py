from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Pay





def home_view(request):
    return render(request, 'payment/home.html' ,     )
    
def payment_view(request):

    CreditCardNumber=request.POST.get('CreditCardNumber')
    CardHolder=request.POST.get('CardHolder')
    ExpirationDate=request.POST.get('ExpirationDate' )
    SecurityCode=request.POST.get('SecurityCode')
    Amount=request.POST.get('Amount')
    if CreditCardNumber != None:
    
        payment=Pay(CreditCardNumber=CreditCardNumber, CardHolder=CardHolder, ExpirationDate=ExpirationDate,
        SecurityCode=SecurityCode, Amount=Amount)
        payment.save()
         
        return HttpResponseRedirect('/payment/')
    return render(request, 'payment/payment1.html' ,   )


