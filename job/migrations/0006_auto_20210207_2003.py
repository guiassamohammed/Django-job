# Generated by Django 3.1.6 on 2021-02-07 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20210207_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Category',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='job.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]