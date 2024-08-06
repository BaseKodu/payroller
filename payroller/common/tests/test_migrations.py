# payroller/common/tests/test_migrations.py
from django.test import TestCase
from django.apps import apps
from django.conf import settings
import os
import pandas as pd
import unittest


class CityMigrationTest(TestCase):

    def setUp(self):
        # Clear existing data
        City = apps.get_model('common', 'City')
        Province = apps.get_model('common', 'Province')
        Country = apps.get_model('common', 'Country')

        City.objects.all().delete()
        Province.objects.all().delete()
        Country.objects.all().delete()

        # Create a test Excel file
        self.file_path = os.path.join(settings.BASE_DIR, 'payroller', 'common', 'migrations', 'files', 'test_worldcities.xlsx')
        data = {
            'city': ['Test City 1', 'Test City 2'],
            'city_ascii': ['Test City 1', 'Test City 2'],
            'lat': [-26.2044, -33.9253],
            'lng': [28.0456, 18.4239],
            'country': ['Test Country', 'Test Country'],
            'iso2': ['TC', 'TC'],
            'iso3': ['TCO', 'TCO'],
            'province': ['Test Province', 'Test Province'],
            'capital': ['admin', 'primary'],
            'population': [8500000, 4770313],
            'id': [1, 2]
        }
        df = pd.DataFrame(data)
        df.to_excel(self.file_path, index=False)

    @unittest.skip("Skip this test, Come back to it later")
    # https://chatgpt.com/g/g-LCO79N7QT-django-copilot/c/f51346f5-57f3-4442-af78-924d1fdb7b35
    def test_city_data_import(self):
        # Import the models
        Country = apps.get_model('common', 'Country')
        Province = apps.get_model('common', 'Province')
        City = apps.get_model('common', 'City')

        # Run the migration
        from django.core.management import call_command

        call_command('migrate', 'common', '0006_import_city_data')

        # Verify the data
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(Province.objects.count(), 1)
        self.assertEqual(City.objects.count(), 2)

        country = Country.objects.get(name='Test Country')
        self.assertEqual(country.iso2, 'TC')
        self.assertEqual(country.iso3, 'TCO')

        province = Province.objects.get(name='Test Province')
        self.assertEqual(province.country, country)

        city1 = City.objects.get(name='Test City 1')
        self.assertEqual(city1.province, province)
        self.assertEqual(city1.latitude, -26.2044)
        self.assertEqual(city1.longitude, 28.0456)

        city2 = City.objects.get(name='Test City 2')
        self.assertEqual(city2.province, province)
        self.assertEqual(city2.latitude, -33.9253)
        self.assertEqual(city2.longitude, 18.4239)

    def tearDown(self):
        # Clean up by removing the test file created
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
