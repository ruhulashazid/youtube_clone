from django import forms
from channel.models import Community
from core.models import Video

class VideoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'id':"title", 'onkeyup':"titleValidate()"}))
    description = forms.CharField(widget=forms.Textarea(attrs={'id':"description", 'onkeyup':"desc_validate()"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':"file"}))
    video = forms.FileField(widget=forms.FileInput(attrs={'class':"file"}))

    class Meta:
        model = Video
        fields = ['video', 'image', 'title', 'description', 'tags', 'visibility']


class CommunityForm(forms.ModelForm):

    class Meta:
        model = Community
        fields = ['content', 'image']
