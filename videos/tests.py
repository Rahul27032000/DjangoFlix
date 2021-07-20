from django.test import TestCase
from .models import Video
from django.utils import timezone
from django.utils.text import slugify

# Create your tests here.
class VideoModelTestCase(TestCase):
    def setUp(self):
        self.obj_a = Video.objects.create(title='this is my new title', video_id='abc')
        self.obj_b = Video.objects.create(title='this is my new title', state=Video.VideoStateOptions.PUBLISH, video_id='abcd')


    def test_sluf_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug,self.obj_a.slug)



    def test_valid_title(self):
        title='this is my new title'
        qs = Video.objects.filter(title=title, video_id='abc')
        self.assertTrue(qs.exists())


    def test_create_count(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(),2)

    def test_draft_test(self):
        qs=Video.objects.filter(state=Video.VideoStateOptions.DRAFT)
        self.assertEqual(qs.count(),1)


    def test_published_test(self):
        qs=Video.objects.filter(state=Video.VideoStateOptions.PUBLISH)
        now =timezone.now()
        published_qs= Video.objects.filter(
            state=Video.VideoStateOptions.PUBLISH,
            published_timestamp__lte=now
            )
        self.assertTrue(published_qs.exists())


    def test_publish_manager(self):
        published_qs = Video.objects.all().published()
        published_qs_1 = Video.objects.published()
        self.assertTrue(published_qs_1.exists())
        self.assertEqual(published_qs.count(), published_qs_1.count())


