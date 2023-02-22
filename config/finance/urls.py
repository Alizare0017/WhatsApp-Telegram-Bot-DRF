from django.urls import path
from . import views

urlpatterns = [
    path('sell/',views.SellView.as_view(), name='sell'),
    path('factor/',views.FactorView.as_view(),name='factor')
]
