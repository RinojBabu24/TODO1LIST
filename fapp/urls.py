from django.urls import path
from django.contrib import admin
from . import views
app_name='fapp'


urlpatterns = [
    path('',views.demo,name='demo'),
    path('insert/',views.insert,name='insert'),
    path('edit_task/<int:todo_id>/',views.edit,name='edit'),
    path('update_task/<int:todo_id>/',views.update,name='update'),
    # path('insert_task/<int:todo_id>/',views.insert_task,name='insert'),
    path('insert_task/<int:todo_id>/',views.insert,name='insert'),
    path('delete/<int:id>/',views.delete,name='delete')

]
