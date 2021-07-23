from django.db import models
from django.utils import timezone
from django.utils.text import slugify 
from django.db.models.signals import pre_save
 
# created models here
from netflix.db.models import PublishStateOptions
from netflix.db.receivers import slugify_pre_save, publish_state_pre_save

# Create your models here.
class VideoQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            state=PublishStateOptions.PUBLISH,
            published_timestamp__lte=now
            )

class VideoManger(models.Manager):
    def get_quesryset(self):
        return VideoQuerySet(self.model , using=self._db)


    def published(self):
        return self.get_quesryset().published()



class Video(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True, null=True) # this is my video
    video_id = models.CharField(max_length=220, unique=True)
    active = models.BooleanField(default=True)
    published_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True , null=True)
    state =models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects= VideoManger()




    @property
    def is_published(self):
        return self.active



    # def save(self, *args, **kwargs):
        # if self.state == self.VideoStateOptions.PUBLISH and self.published_timestamp is None:
        #     print("save as timestamp for published")
        #     self.published_timestamp = timezone.now()
        # elif self.state == self.VideoStateOptions.DRAFT:
        #     self.published_timestamp = None
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        # super().save(*args, **kwargs)




class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'



class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Piblished Video'
        verbose_name_plural = 'Piblished Videos'



# creating and connecting signals
pre_save.connect(publish_state_pre_save, sender=Video)
pre_save.connect(slugify_pre_save, sender=Video)