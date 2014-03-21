#from .views import LoginView
from .views import UserViewSet

from django.conf.urls import patterns, include, url

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls
#urlpatterns = patterns('',
    #url(r'^login/$', LoginView.as_view(), name='account-login')
#    url(r'^users/', UserViewSet.as_view({'get': 'list'})),
#)
