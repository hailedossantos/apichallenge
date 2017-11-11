from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^towns/$', views.TownsView.as_view(), name="towns"),
    url(r'^aggs/$', views.AggregationView.as_view(), name="aggregate")
]
