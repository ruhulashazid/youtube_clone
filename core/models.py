from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings

User = settings.AUTH_USER_MODEL

VISIBILITY =  (
    ("private", "Private"),
    ("unlisted", "Unlisted"),
    ("members_only", "Members Only"),
    ("public", "Public")
)

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

class Video(models.Model):
    video = models.FileField(upload_to=user_directory_path)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    title = models.CharField(max_length=100) 
    description = models.TextField(null=True, blank=True)
    tags = TaggableManager()
    date = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(choices=VISIBILITY, max_length=100, default="public")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name="likes")

    # Add Featured Field
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)

    def __ste__(self):
        return self.comment[:30]