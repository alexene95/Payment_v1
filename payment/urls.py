from payment.views  import   payment_view , home_view
from django.urls import path
from django.contrib import admin 



urlpatterns = [
    path('payment/', home_view, name='home_view'),
    path ('' , payment_view , name='payment_view'),

]
