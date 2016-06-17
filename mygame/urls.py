from django.conf.urls import url
from mygame.views import Selectcard
urlpatterns = [
    url(r'^game/$', 'mygame.views.Selectcard'),
    url(r'^$', 'mygame.views.Loadhomepage'),
    url(r'^post/$', 'mygame.views.Start'),
]