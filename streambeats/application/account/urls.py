from .views import LoginView
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='account-login')
)
