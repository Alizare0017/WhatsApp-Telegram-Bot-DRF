from django.urls import path
from . import views


app_name = 'payment'
urlpatterns = [
    path('request/', views.send_request.as_view(), name='request'),
    path('verify/', views.verify , name='verify'),
]