from django.db import models
from django.utils import timezone
from django.utils.text import slugify 
from django.db.models.signals import pre_save
 
# created models here
from netflix.db.models import PublishStateOptions
from netflix.db.receivers import slugify_pre_save, publish_state_pre_save
from videos.models import Video

# Create your models here.
class PlaylistQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            state=PublishStateOptions.PUBLISH,
            published_timestamp__lte=now
            )

class PlaylistManger(models.Manager):
    def get_quesryset(self):
        return PlaylistQuerySet(self.model , using=self._db)


    def published(self):
        return self.get_quesryset().published()



class Playlist(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True, null=True) # this is my video
    active = models.BooleanField(default=True)
    video = models.ForeignKey(Video,null=True, on_delete=models.SET_NULL) #one video per playlist
    published_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True , null=True)
    state =models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects= PlaylistManger()




    @property
    def is_published(self):
        return self.active




# creating and connecting signals
pre_save.connect(publish_state_pre_save, sender=Playlist)
pre_save.connect(slugify_pre_save, sender=Playlist)