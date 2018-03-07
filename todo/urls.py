from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', get_index, name="todo_index"),
    url(r'edit/(\d+)$', edit_todo_item, name="todo_edit"),
    url(r'delete/(\d+)$', delete_todo_item, name="make_todo_go_bye_bye"),
    url(r'toggle/(\d+)$', toggle_status, name="todo_toggle"),
]
