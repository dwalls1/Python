from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^retriveposts/(?P<myword>[a-zA-Z]+)$', views.retrivePosts, name='retrivepost'),
    # start of my url film star dw
    url(r'^filmstar/', views.filmstar, name='filmstar'),
    # end of my url dw
    url(r'^students/', views.students, name='students'),
    
    # start of my url submit  dw
    url(r'^cost/$', views.costView, name='cost' ),
    # end of my submit url dw
]