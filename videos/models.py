from django.db import models
from django.utils import timezone
from django.utils.text import slugify 

# Create your models here.
class VideoQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            state = Video.VideoStateOptions.PUBLISH,
            published_timestamp__lte = now
        )

class VideoManger(models.manager):
    def get_quesryset(self):
        return VideoQuerySet(self.model,using=self._db)





class Video(models.Model):
    class VideoStateOptions(models.TextChoices):
        # Constant = DB_value , USER_DISPLAY_VA
        # UNLISTED = 'UN','Unlisted'
        PUBLISH = 'PU','Published'
        DRAFT = 'DR','Draft'
         


    title = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True, null=True) # this is my video
    video_id = models.CharField(max_length=220, unique=True)
    active = models.BooleanField(default=True)
    published_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True , null=True)
    state =models.CharField(max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def is_published(self):
        return self.active



    def save(self, *args, **kwargs):
        if self.state == self.VideoStateOptions.PUBLISH and self.published_timestamp is None:
            print("save as timestamp for published")
            self.published_timestamp = timezone.now()
        elif self.state == self.VideoStateOptions.DRAFT:
            self.published_timestamp = None
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)




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

