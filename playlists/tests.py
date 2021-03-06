from django.test import TestCase
from .models import Playlist
from netflix.db.models import PublishStateOptions
from django.utils import timezone
from django.utils.text import slugify
from videos.models import Video

# Create your tests here.
class PlaylistModelTestCase(TestCase):
    def setUp(self):
        video_a = Video.objects.create(title='This is my first video', video_id='something')
        self.video_a = video_a
        self.obj_a = Playlist.objects.create(title='this is my new title', video = video_a)
        self.obj_b = Playlist.objects.create(title='this is my new title', state= PublishStateOptions.PUBLISH, video = video_a )


    def test_video_playlist(self):
        qs = self.video_a.platlist_set.all()
        self.assertEqual(qs.count(),2)
        
        
        

    def test_sluf_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug,self.obj_a.slug)



    def test_valid_title(self):
        title='this is my new title'
        qs = Playlist.objects.filter(title=title)
        self.assertTrue(qs.exists())


    def test_create_count(self):
        qs = Playlist.objects.all()
        self.assertEqual(qs.count(),2)

    def test_draft_test(self):
        qs=Playlist.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(),1)


    def test_published_test(self):
        qs=Playlist.objects.filter(state=PublishStateOptions.PUBLISH)
        now =timezone.now()
        published_qs= Playlist.objects.filter(
            state=PublishStateOptions.PUBLISH,
            published_timestamp__lte=now
            )
        self.assertTrue(published_qs.exists())


    def test_publish_manager(self):
        # published_qs = Playlist.objects.all().published()
        published_qs_1 = Playlist.objects.published()
        self.assertTrue(published_qs_1.exists())
        # self.assertEqual(published_qs.count(), published_qs_1.count())


