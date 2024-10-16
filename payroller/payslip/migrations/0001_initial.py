# Generated by Django 5.0.9 on 2024-10-14 14:59

import django.db.models.deletion
import django.db.models.expressions
import djmoney.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0003_alter_employee_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyContributions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uif_currency', djmoney.models.fields.CurrencyField(choices=[('ZAR', 'South African Rand')], default='ZAR', editable=False, max_length=3)),
                ('uif', djmoney.models.fields.MoneyField(decimal_places=4, max_digits=19)),
                ('sdl_currency', djmoney.models.fields.CurrencyField(choices=[('ZAR', 'South African Rand')], default='ZAR', editable=False, max_length=3)),
                ('sdl', djmoney.models.fields.MoneyField(decimal_places=4, max_digits=19)),
                ('total', models.GeneratedField(db_persist=True, expression=django.db.models.expressions.CombinedExpression(models.F('uif'), '+', models.F('sdl')), output_field=djmoney.models.fields.MoneyField(decimal_places=4, max_digits=19))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Deductions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('paye_currency', djmoney.models.fields.CurrencyField(choices=[('ZAR', 'South African Rand')], default='ZAR', editable=False, max_length=3)),
                ('paye', djmoney.models.fields.MoneyField(decimal_places=4, max_digits=19)),
                ('uif_currency', djmoney.models.fields.CurrencyField(choices=[('ZAR', 'South African Rand')], default='ZAR', editable=False, max_length=3)),
                ('uif', djmoney.models.fields.MoneyField(decimal_places=4, max_digits=19)),
                ('medical_aid_currency', djmoney.models.fields.CurrencyField(choices=[('ZAR', 'South African Rand')], default='ZAR', editable=False, max_length=3)),
                ('medical_aid', djmoney.models.fields.MoneyField(decimal_places=4, max_digits=19)),
                ('total', models.GeneratedField(db_persist=True, expression=django.db.models.expressions.CombinedExpression(django.db.models.expressions.CombinedExpression(models.F('paye'), '+', models.F('uif')), '+', models.F('medical_aid')), output_field=djmoney.models.fields.MoneyField(decimal_places=4, max_digits=19))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Earnings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('basic_salary_currency', djmoney.models.fields.CurrencyField(choices=[('ZAR', 'South African Rand')], default='ZAR', editable=False, max_length=3)),
                ('basic_salary', djmoney.models.fields.MoneyField(decimal_places=4, max_digits=19)),
                ('commission_currency', djmoney.models.fields.CurrencyField(choices=[('ZAR', 'South African Rand')], default='ZAR', editable=False, max_length=3)),
                ('commission', djmoney.models.fields.MoneyField(decimal_places=4, max_digits=19)),
                ('total', models.GeneratedField(db_persist=True, expression=django.db.models.expressions.CombinedExpression(models.F('basic_salary'), '+', models.F('commission')), output_field=djmoney.models.fields.MoneyField(decimal_places=4, max_digits=19))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('company_contributions', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payslip', to='payslip.companycontributions')),
                ('deductions', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payslip', to='payslip.deductions')),
                ('earnings', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payslip', to='payslip.earnings')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payslips', to='employees.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
