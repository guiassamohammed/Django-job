# Generated by Django 3.1.6 on 2021-02-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]