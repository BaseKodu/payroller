# Generated by Django 5.0.9 on 2024-10-16 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_created_at_company_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPayrollSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_period', models.CharField(choices=[('M', 'Monthly'), ('W', 'Weekly'), ('BW', 'Bi-Weekly'), ('SM', 'Semi-Monthly'), ('A', 'Annually'), ('D', 'Daily')], default='M', max_length=2)),
                ('monthly_payment_day', models.IntegerField(default=25, help_text='Day of the month for payment. Use negative numbers for end-of-month counting.')),
                ('weekly_payment_day', models.IntegerField(blank=True, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], null=True)),
                ('semi_monthly_first_day', models.IntegerField(default=1, help_text='First payment day for semi-monthly payments')),
                ('semi_monthly_second_day', models.IntegerField(default=15, help_text='Second payment day for semi-monthly payments')),
                ('pay_on_weekends_holidays', models.BooleanField(default=False, help_text='Whether to make payments on weekends and public holidays')),
                ('weekend_holiday_behavior', models.CharField(choices=[('PO', 'Pay on weekend/holiday'), ('PB', 'Pay before weekend/holiday'), ('PA', 'Pay after weekend/holiday')], default='PB', help_text='Behavior when payment falls on a weekend or holiday', max_length=2)),
                ('short_month_behavior', models.CharField(choices=[('PO', 'Pay on weekend/holiday'), ('PB', 'Pay before weekend/holiday'), ('PA', 'Pay after weekend/holiday')], default='PB', help_text="Behavior when payment day doesn't exist in a shorter month", max_length=2)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='company.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PayrollPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('default_start_day', models.DateField(default=1)),
                ('default_end_day', models.DateField(default=31)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
