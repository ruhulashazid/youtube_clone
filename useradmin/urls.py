from django.urls import path
from useradmin import views


urlpatterns = [
    path("", views.Studio, name="studio"),
    path("Video_delete/<vid>/", views.Video_delete, name="video-delete")
]