from django.urls import path, include
from catalog import views

app_name = 'catalog'

guitar_patterns = [
    path('acoustic_gt/', views.ac_gt, name = 'Ac_gt'),
    path('bass_gt/', views.bass_gt_ListView.as_view(), name = 'Bass_gt'),
    path('electro_gt/', views.electro_gt, name = 'Electro_gt'),
]

dops_patterns = [
    path('strings/', views.strings, name = 'Strings'),
    path('mediators/', views.mediators, name = 'Mediators'),
    path('capo/', views.capo, name = 'Capo'),
    path('others/', views.others_ListView.as_view(), name = 'Others'),
]

urlpatterns = [
    path('', views.main, name = 'Main'),
    path('dops/', views.dops, name = 'Dops'),
    path('dops/', include(dops_patterns)),
    path('guitars/', views.guitars_ListView.as_view(), name = 'Guitars'),
    path('guitars/', include(guitar_patterns)),
]
