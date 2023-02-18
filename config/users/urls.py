from django.urls import path
from . import views

urlpatterns = [
    path('',views.InfoView.as_view(), name='info'),
    path('charge/',views.ChangeView.as_view(),name='change'),
]
