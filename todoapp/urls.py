from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/complete", views.complete, name="complete"),
    path("<int:task_id>/remove", views.remove, name="remove")
]