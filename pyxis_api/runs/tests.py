from django.test import TestCase
from runs.models import Run

# Create your tests here.

class RunsApiTestCase(TestCase):

    def setUp(self):
        run = Run.objects.create(id='1234', passes=80, fails=12, skips=8)

    def tearDown(self):
        Run.objects.all().delete()

    def test_it_should_get_all_runs(self):
        response = self.client.get('/runs/')
        self.assertEqual(response.status_code, 200)
