# Generated by Django 2.0.1 on 2018-10-21 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20181019_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='VWInputType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_Short', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='input_answer',
            name='input',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='input_answer',
            name='input_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input', to='main.Input_Title'),
        ),
        migrations.AddField(
            model_name='input_title',
            name='vw_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.VWInputType'),
        ),
    ]
