# Generated by Django 5.0.3 on 2024-03-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_bidding_payment_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidding',
            name='p_status',
            field=models.CharField(choices=[('pending', 'pending'), ('done', 'done'), ('offline', 'offline')], default='pending', max_length=50),
        ),
    ]
