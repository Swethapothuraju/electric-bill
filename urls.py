from django.conf.urls import url
from . import views
app_name = 'billapp'
urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^reg$', views.reg,name='reg'),
    url(r'^login$',views.login,name='login'),
    url(r'^location$', views.location,name='location'),
    url(r'^payment$',views.payment,name='payment'),
    ]
