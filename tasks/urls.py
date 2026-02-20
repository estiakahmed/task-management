from django.urls import path
from tasks.views import showTask,show_specific_task
urlpatterns = [
    path("show-task",showTask),
    path("show-task/<id>",show_specific_task)
]