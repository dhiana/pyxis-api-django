import json
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

    def test_it_should_allow_no_trailing_slash(self):
        response = self.client.get('/runs')
        self.assertEqual(response.status_code, 301)

    def test_it_should_rerurn_a_collection_of_runs(self):
        response = self.client.get('/runs/')
        response_dict = json.loads(response.content)
        run = response_dict['runs'].pop()
        self.assertEqual(run['id'], '1234')
        self.assertEqual(run['passes'], 80)
        self.assertEqual(run['fails'], 12)
        self.assertEqual(run['skips'], 8)
        self.assertEqual(run['success_percentage'], 80)

    def test_it_should_get_a_specific_run(self):
        response = self.client.get('/runs/1234/')
        self.assertEqual(response.status_code, 200)
