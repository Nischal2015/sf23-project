# Generated by Django 3.2.13 on 2022-07-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseTracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='remarks',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
