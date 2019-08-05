from django.test import TestCase

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.test_profile = profile(images=list('Beautiful butterflies'))
        self.test_profile.save_profile()

       

    def tearDown(self):
       profile.objects.all().delete()