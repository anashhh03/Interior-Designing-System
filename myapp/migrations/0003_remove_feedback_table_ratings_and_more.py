# Generated by Django 4.1.1 on 2023-04-21 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_bidding_rejected_bidding_show_interest_button_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback_table',
            name='RATINGS',
        ),
        migrations.RemoveField(
            model_name='feedback_table',
            name='login_id',
        ),
        migrations.AddField(
            model_name='feedback_table',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='feedback_table',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='feedback_table',
            name='subject',
            field=models.CharField(default='', max_length=300),
        ),
    ]
