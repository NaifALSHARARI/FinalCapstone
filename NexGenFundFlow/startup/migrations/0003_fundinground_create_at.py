# Generated by Django 4.2.7 on 2024-01-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0002_remove_fundinground_fund_current_close_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundinground',
            name='create_at',
            field=models.DateField(auto_now_add=True, default="2017-10-1"),
            preserve_default=False,
        ),
    ]
