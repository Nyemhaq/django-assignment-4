from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name = 'add_task'), 
    path('', views.task, name = 'task'), 
    path('edit/<int:id>', views.edit_task, name = 'edit_task'), 
    path('delete/<int:id>', views.delete, name = 'delete'), 
    
]
