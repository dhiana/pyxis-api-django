from django.test import TestCase
from runs.models import Run

# Create your tests here.

class RunsApiTestCase(TestCase):

    def setUp(self):
        # Arrange
        run = Run.objects.create(id='1234', passes=80, fails=12, skips=8)

    def test_it_should_get_all_runs(self):
        # Act
        response = self.client.get('/runs')
        # Assert
        self.assertEqual(response.status_code, 200)
