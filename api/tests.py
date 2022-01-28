from rest_framework.test import APITestCase
from .models import Tasks

# Create your tests here.

class TestCRUD(APITestCase):
    def test_str(self):
        task = Tasks.objects.create(title="First",date="2020-01-22",completed=True)
        self.assertEqual(task.__str__(),"First")
        