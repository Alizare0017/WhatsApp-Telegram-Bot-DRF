from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('',views.InfoView.as_view(), name='info'),
    path('change/',views.ChangeView.as_view(),name='change'),
]
