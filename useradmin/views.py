from django.shortcuts import render
from channel.models import Channel
from core.models import Video, Comment
from django.contrib.auth.decorators import login_required


@login_required
def Studio(request):
    user = request.user
    channel = user.channel

    channel = Channel.objects.get(user=user)
    videos = Video.objects.filter(user=user)
    comments = Comment.objects.filter()

    context = {
        "user":user,
        "channel":channel,
        "videos":videos,
    }

    return render(request, "useradmin/studio.html", context)


def Video_delete(request, vid):
    user = request.user
    video = Video.objects.get(id=vid, user=user)
    video.delete()

