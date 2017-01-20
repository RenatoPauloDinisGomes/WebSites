from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Cursos/$',views.Cursos,name='Cursos'),
    url(r'^Cursos/(?P<pk>\d+)/', views.CadeirasCurso),
    url(r'^Cadeiras/(?P<pk>\d+)/$', views.CadeirasCurso)

]