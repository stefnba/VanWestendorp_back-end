# Generated by Django 2.0.1 on 2018-10-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('exo_toocheap', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('exo_cheap', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('exo_epensive', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('exo_tooexpensive', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('basis_toocheap', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('basis_cheap', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('basis_epensive', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('basis_tooexpensive', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('plus_toocheap', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('plus_cheap', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('plus_epensive', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('plus_tooexpensive', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('dvv_toocheap', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('dvv_cheap', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('dvv_epensive', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('dvv_tooexpensive', models.DecimalField(decimal_places=2, max_digits=1000)),
            ],
        ),
    ]