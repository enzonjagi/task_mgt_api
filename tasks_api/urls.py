from django.urls import path
from .views import TaskListApiView
from django.conf import settings

urlpatterns = [
    path('', TaskListApiView.as_view()),
    # path('api/<int:task_id>'),
]