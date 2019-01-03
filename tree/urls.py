from django.urls import path

from .views import *


urlpatterns = [
    path('', emp_tree),
    path('not_authenticated/', not_authenticated, name='not_authenticated_url'),
    path('tree/', emp_tree, name='emp_tree_url'),
    path('table/', emp_table, name='emp_table_url'),
    path('ajaxtable', ajax_table),
    path('ajaxtree', ajax_tree),
    path('ajaxdragdrop', ajax_dragdrop),
    path('get-empl-photo', get_empl_photo),
    path('logout_', logout_, name='logout_url'),
]
