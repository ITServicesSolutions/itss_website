from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='administration'),
    path('site', our_site, name='site'),
    path('site/logo', logo_list, name='logo_list'),
    path('site/logo/add', logo_form, name='logo_add'),
    path('site/carousel', carousel_list, name='carousel_list'),
    path('site/carousel/add', carousel_form, name='carousel_add'),
    path('site/comments', comments_list, name='comments_list'),
    path('site/comment/add', comment_add, name='comment_add'),
    path('site/partner', partner_list, name='partner_list'),
    path('formations', formation, name='formation'),
    path('formations/add', add_formation, name='add_formation'),
    path('partners', partners_list, name='partners_list'),
    path('formations/add', partner_add, name='partner_add'),
]
