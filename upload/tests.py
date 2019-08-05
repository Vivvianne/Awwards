from django.test import TestCase
from . models import Post

# Create your tests here.

class PostTestClass(TestCase):
    def setUp(self):
        self.test_post = image(images=list('Beautiful butterflies'))
        self.test_post.save_post()

        self.image = Post(id=1,description="Slide Away")
        self.image.save_image()

    def tearDown(self):
       Post.objects.all().delete()