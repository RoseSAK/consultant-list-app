from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^manager_home/$', views.manager_home, name='manager_home'),

    url(r'^search_candidates/$', views.search_candidates, name='search_candidates'),

    url(r'^candidate_detail/$', views.candidate_detail, name='candidate_detail'),

    url(r'^candidate_detail/(?P<candidate_id>\w+)$', views.candidate_detail, name='candidate_detail'),

    url(r'^edit_candidate/$', views.edit_candidate, name='edit_candidate'),

    url(r'^edit_candidate/(?P<candidate_id>\w+)$', views.edit_candidate, name='edit_candidate'),

    url(r'^consultant_database/$', views.consultant_database, name='consultant_database'),

    url(r'^view_all/$', views.view_all, name='view_all'),

    url(r'^view_selection/$', views.view_selection, name='view_selection'),

    url(r'^delete_candidate/(?P<candidate_id>\w+)$', views.delete_candidate, name='delete_candidate'),



]