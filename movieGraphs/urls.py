from django.conf.urls import url
from movieGraphs import views


urlpatterns = [
    url(r'^$', views.film, name='film'),                  
    url(r'^sample.png/$', views.sample_graph, name='sample_graph'),
    url(r'^sample_graph/$', views.detail, name='detail'),
    url(r'^get_graph/$', views.film_graph, name='get_graph'),
]