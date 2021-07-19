from django.contrib import admin
from django.db.models.base import Model
from .models import Video, VideoPublishedProxy, VideoAllProxy

# Register your models here.

class VideoAllAdmin(admin.ModelAdmin):
    list_display= ['title','state', 'video_id','is_published','published_timestamp','timestamp','updated']
    search_fields=['title']
    list_filter=['active','state']
    readonly_fields=['title','published_timestamp']
    class Meta:
        model = VideoAllProxy

    # def published(self,obj,*args, **kwargs):
    #     print(args, kwargs,)
    #     return obj.active


class VideoPublishedProxyadmin(admin.ModelAdmin):
    list_display= ['title', 'video_id']
    search_fields=['title']
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)

admin.site.register(VideoAllProxy, VideoAllAdmin)
admin.site.register(VideoPublishedProxy,VideoPublishedProxyadmin)
