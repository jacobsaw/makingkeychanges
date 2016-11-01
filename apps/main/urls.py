from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^services/$', views.services, name='services'),
    url(r'^lori_testimonials/$', views.lori_testimonials, name='lori_testimonials'),
    url(r'^marci_testimonials/$', views.marci_testimonials, name='marci_testimonials'),
    url(r'^lori_engagements/$', views.lori_engagements, name='lori_engagements'),
    url(r'^marci_engagements/$', views.marci_engagements, name='marci_engagements'),
    url(r'^lori_publications/$', views.lori_publications, name='lori_publications'),
    url(r'^marci_publications/$', views.marci_publications, name='marci_publications'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^online_resources/$', views.online_resources, name='online_resources'),
    url(r'^community_ensembles/$', views.community_ensembles, name='community_ensembles'),
    url(r'^composer_connections/$', views.composer_connections, name='composer_connections'),
    url(r'^HCPSS_MS_GT_Band/$', views.hcpss, name='hcpss'),
    url(r'^instrument_repairs/$', views.instrument_repairs, name='instrument_repairs'),
    url(r'^private_lessons/$', views.private_lessons, name='private_lessons'),
    url(r'^recommended_equipment/$', views.recommended_equipment, name='recommended_equipment'),
    url(r'^study_recordings/$', views.study_recordings, name='study_recordings'),
    url(r'^summer_band_camps/$', views.summer_band_camps, name='summer_band_camps'),
]