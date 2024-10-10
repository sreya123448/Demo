from django.urls import path
from . import views


urlpatterns = [
    path('todo/',views.Todo,name='todo'),
    path('list',views.list,name='list'),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.Todoedit)
]