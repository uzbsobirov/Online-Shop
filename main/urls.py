from django.urls import path
from .views import *


urlpatterns = [
    path('', BasePage.as_view(), name='basepage'),
    path('products/', ProductView.as_view(), name='productview')
]