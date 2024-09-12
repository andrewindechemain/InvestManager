# Generated by Django 5.1.1 on 2024-09-11 14:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accountpermissions_user_alter_account_users_and_more'),
        ('transactions', '0002_alter_transaction_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('investment_type', models.CharField(choices=[('stock', 'Stock'), ('bond', 'Bond'), ('mutual_fund', 'Mutual Fund'), ('etf', 'ETF')], max_length=20)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tax_rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], default='none', max_length=10),
        ),
        migrations.CreateModel(
            name='InterestReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interest_returns', to='accounts.account')),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.investment')),
            ],
        ),
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_basis', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holdings', to='accounts.account')),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.investment')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='investment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transactions.investment'),
        ),
    ]