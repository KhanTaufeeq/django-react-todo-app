from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.list_tasks, name = 'list_tasks'),
    path('add/', views.add_task, name = 'add_task'),
    path('edit/<int:id>/', views.edit_task, name = 'edit_task'),
    path('delete/<int:id>/', views.delete_task, name = 'delete_task'),
]
