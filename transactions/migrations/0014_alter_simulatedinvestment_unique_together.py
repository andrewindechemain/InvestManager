# Generated by Django 5.1.1 on 2024-09-16 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_account_investment_value'),
        ('transactions', '0013_remove_simulatedinvestment_investment_type'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='simulatedinvestment',
            unique_together={('account', 'symbol')},
        ),
    ]