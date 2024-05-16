from django.contrib import admin
from core.models import Video, Comment
from import_export.admin import ImportExportModelAdmin

class VideoAdmin(ImportExportModelAdmin):
    pass

class CommentAdmin(ImportExportModelAdmin):
    list_display = ["user", "comment", "active", "video"]

admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)