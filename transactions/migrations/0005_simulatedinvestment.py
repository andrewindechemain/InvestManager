# Generated by Django 5.1.1 on 2024-09-14 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_balance'),
        ('transactions', '0004_remove_transaction_investment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimulatedInvestment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('units', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=10)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simulated_investments', to='accounts.account')),
            ],
        ),
    ]