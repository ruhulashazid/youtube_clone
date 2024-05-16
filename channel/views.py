from django.shortcuts import render, get_object_or_404, redirect
from channel.models import Channel, Community, CommunityComment
from core.models import Video
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from channel.forms import VideoForm, CommunityForm



def channel_profile(request, channel_name):
    channel = get_object_or_404(Channel, id=channel_name)

    # Getting Popular Videos
    videos = Video.objects.filter(user=channel.user, visibility="public").order_by("-views")
    try:
        video_featured = Video.objects.get(user=channel.user.id, featured=True)
    except:
        
        video_featured = None
        # messages.warning(request, f"Only one video can be featured!")
        
    context = {
        "videos":videos,
        "channel":channel,
        "video_featured":video_featured
    }

    return render(request, "channel/channel.html", context)

def channel_videos(request, channel_name):
    channel = get_object_or_404(Channel, id=channel_name)
    videos = Video.objects.filter(user=channel.user, visibility="public").order_by("-date")
        
    context = {
        "videos":videos,
        "channel":channel,
    }

    return render(request, "channel/channel-videos.html", context)


def channel_about(request, channel_name):
    channel = get_object_or_404(Channel, id=channel_name)
        
    context = {
        "channel":channel,
    }

    return render(request, "channel/channel-about.html", context)


def channel_community(request, channel_name):
    channel = get_object_or_404(Channel, id=channel_name)
    community = Community.objects.filter(channel=channel, status="active").order_by("-date")

    context = {
        "community":community,
        "channel":channel,
    }

    return render(request, "channel/channel-community.html", context)


def channel_community_detail(request, channel_name, community_id):
    channel = get_object_or_404(Channel, id=channel_name)
    community = Community.objects.get(channel=channel, id=community_id, status="active")

    # Listing all Comments for a community post
    comments = CommunityComment.objects.filter(active=True, community=community).order_by("-date")

    context = {
        "community":community,
        "comments":comments,
        "channel":channel,
    }

    return render(request, "channel/channel-community-detail.html", context)


@login_required
def create_comment(request, community_id):

    if request.method == "POST":
        community = Community.objects.get(id=community_id, status="active")
        comment = request.POST.get("comment")
        user = request.user 

        new_comment = CommunityComment.objects.create(community=community, user=user, comment=comment)
        new_comment.save()
        messages.success(request, f"Comment Posted.")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def delete_comment(request, community_id, comment_id):
    community = Community.objects.get(id=community_id)
    comment = CommunityComment.objects.get(id=comment_id, community=community)

    comment.delete()
    messages.success(request, f"Comment Deleted.")

    return redirect("channel-community-detail", community.channel.id, community.id)

@login_required
def like_community_post(request, community_id):
    community = Community.objects.get(id=community_id)
    user = request.user

    if user in community.likes.all():
        community.likes.remove(user)
    else:
        community.likes.add(user)
    
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def video_upload(request):
    user = request.user
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.save()
            form.save_m2m()
            messages.success(request, f"Video Uploaded Successfully.")
            return redirect("studio")
    else:
        form = VideoForm()
    context = {
        "form":form,
    }
    return render(request, "channel/upload-video.html", context)



@login_required
def video_edit(request, channel_id, video_id):
    video = Video.objects.get(id=video_id)
    channel = Channel.objects.get(id=channel_id)
    user = request.user


    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.save()
            form.save_m2m()
            messages.success(request, f"Video Edited Successfully.")
            return redirect("studio")
    else:
        form = VideoForm(instance=video)
    context = {
        "form":form,
        "video":video,
    }
    return render(request, "channel/upload-video.html", context)


@login_required
def video_delete(request, video_id):
    video = Video.objects.get(id=video_id)
    user = request.user

    if request.user == video.user:
        video.delete()
        return redirect("studio")
    else:
        return HttpResponse("You are not allowed to delete this video")



@login_required
def create_community_post(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    user = request.user 

    if request.method == "POST":
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.channel = channel
            new_form.save()
            post_id = new_form.id
            messages.success(request, "Post Created.")
            return redirect("channel-community-detail", channel.id, post_id)
    else:
        form = CommunityForm()
    context = {
        "form":form,
    }
    return render(request, "channel/create-post.html", context)



@login_required
def edit_community_post(request, channel_id, community_post_id):
    channel = Channel.objects.get(id=channel_id)
    post = Community.objects.get(id=community_post_id)
    user = request.user 

    if request.method == "POST":
        form = CommunityForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.channel = channel
            new_form.save()
            post_id = new_form.id
            messages.success(request, "Post Edited.")
            return redirect("channel-community-detail", channel.id, post_id)
    else:
        form = CommunityForm(instance=post)
    context = {
        "form":form,
    }
    return render(request, "channel/create-post.html", context)

@login_required
def delete_comm_post(request, channel_id, post_id):
    channel = Channel.objects.get(id=channel_id)
    post = Community.objects.get(id=post_id)

    post.delete()
    return redirect("channel-community", channel.id)

