# Generated by Django 5.1 on 2025-04-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_income', models.BooleanField(default=False)),
                ('is_expense', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
            ],
        ),
    ]
