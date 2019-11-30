from django.conf.urls import url
from django.urls import include


from ksglapp import views
urlpatterns = [
    url('confirm',views.confirm),
    url('getkey',views.update_key),
    url(r'^$', views.index),
]
