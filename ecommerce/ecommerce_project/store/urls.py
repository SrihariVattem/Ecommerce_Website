from django.urls import path
from .views import *


urlpatterns=[
    path('',store,name='store'),
    path('cart', cart, name='cart'),
    path('cheackout', cheackout, name='cheackout'),
    path('update_item/',updateItem, name="update_item"),
    path('process_order/',processOrder, name="process_order"),


]