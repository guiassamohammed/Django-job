# Generated by Django 3.1.6 on 2021-02-20 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.job'),
            preserve_default=False,
        ),
    ]
