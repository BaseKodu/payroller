# Generated by Django 5.0.9 on 2024-10-12 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('misc', '0002_import_city_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='bank_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='misc.bankaccount'),
        ),
    ]
