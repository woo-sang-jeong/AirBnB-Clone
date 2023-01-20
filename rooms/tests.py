from rest_framework.test import APITestCase


class TestAmenities(APITestCase):
    def test_plus(self):
        self.assertEqual(2 + 2, 4, "wrong!")
