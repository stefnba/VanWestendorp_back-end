# Generated by Django 2.0.1 on 2018-10-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181014_1824'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='answers',
            name='client_segment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
