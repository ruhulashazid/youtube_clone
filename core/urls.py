from django.urls import path
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("trending/", views.trending, name="trending"),
    path("saved-videos/", views.savedVideos, name="saved-videos"),


    path("watch/<int:pk>/", views.videoDetail, name="video-detail"),

    # Saving Comment to db
    path("ajax-save-comment/", views.ajax_save_comment, name="save-comment"),
    path("ajax-delete-comment/", views.ajax_delete_comment, name="delete-comment"),

    # Subscribe Function
    path("add-sub/<int:id>/", views.add_new_subscribers, name="add_sub"),
    path("sub-load/<int:id>/", views.load_channel_subs, name="subLoad"),

    # Like Function
    path("add-like/<int:id>/", views.add_new_like, name="add_like"),
    path("likes-load/<int:id>/", views.load_video_likes, name="likeLoad"),

    # Saving Video TO Profile
    path("save-video/<video_id>/", views.save_video, name="save-video"),

    # Search URL
    path("video/search/", views.searchView, name="search"),

     # Tag URL
    path("tags/video/<slug:tag_slug>", views.tag_list, name="tags"),

]






# urlpatterns = [
    # path("", views.homepage, name="home"),
    # path("about/", views.aboutpage, name="daosjdasjdijaspodjoaspjdoasdjajsodjaosjd"),
    # path("contact/", views.contactpage, name="contact"),
    
# ]