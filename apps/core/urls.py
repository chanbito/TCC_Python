from unicodedata import name
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('<slug:token>', views.home, name='home'),
    path('', views.home, name='home'),
    path('send/',views.sending, name='send'),
    path('returning/',views.returning, name='returning'),
]