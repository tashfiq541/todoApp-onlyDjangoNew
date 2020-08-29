from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('update_task/<int:task_id>/', views.updateTask, name="update"),
    path('delete_task/<int:task_id>/', views.deleteTask, name="delete"),
]
