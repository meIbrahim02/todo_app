from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>', views.task_delete, name="task_delete"),
    path('toggle/<int:pk>', views.task_toggle_complete, name='task_toggle_complete')
]

