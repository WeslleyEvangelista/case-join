from django.test import TestCase
from .models import Target

class TargetModelTest(TestCase):
    def setUp(self):
        Target.objects.create(name="Test Target", latitude=0.0, longitude=0.0, expiration_date="2024-01-01")

    def test_target_creation(self):
        target = Target.objects.get(name="Test Target")
        self.assertEqual(target.name, "Test Target")
        self.assertEqual(target.latitude, 0.0)
        self.assertEqual(target.longitude, 0.0)
        self.assertEqual(target.expiration_date, "2024-01-01")