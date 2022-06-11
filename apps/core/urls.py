from django.urls import path

from . import views, httpRequests

app_name = 'core'

urlpatterns = [
    path('<slug:token>', views.home, name='home'),
    path('', views.home, name='home'),
    path('translater/<mensagem>/',httpRequests.do_GET, name='translater'),
    path('send/',views.sending, name='send'),
    path('returning/',views.returning, name='returning'),
    path('bla/',httpRequests.do_GET, name='translater'),
]