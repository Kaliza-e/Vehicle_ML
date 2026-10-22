from django.test import SimpleTestCase


class DashboardViewTests(SimpleTestCase):
    def test_homepage_renders_vehicle_frequency_table(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Manufacturer")
        self.assertContains(response, "Honda")
