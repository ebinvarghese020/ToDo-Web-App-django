from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edittask/<id>', views.edit_task, name="edit_task"),
    path('newtask', views.create_new_task, name="create_new_task"),
    path('markascomplete/<id>', views.mark_as_complete, name="mark_as_complete"),
    path('markasincomplete/<id>', views.mark_as_incomplete, name="mark_as_incomplete"),
    path('deletetask/<id>', views.delete_task, name="delete_task")
]