from django.conf.urls import url
import views

urlpatterns = [

    url(r'^courses$', views.display),
    url(r'courses/create$', views.create),
    url(r'delete/(?P<id>\d+)$', views.delete),
    url(r'destroy/(?P<id>\d+)$', views.destroy)

]