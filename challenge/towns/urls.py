from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TownsView.as_view(), name="towns"),
]
