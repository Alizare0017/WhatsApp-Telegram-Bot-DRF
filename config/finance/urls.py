from django.urls import path
from . import views



app_name = 'finance'
urlpatterns = [
    path('sell/',views.SellView.as_view(), name='sell'),
    path('factor/',views.FactorView.as_view(),name='factor')
]
