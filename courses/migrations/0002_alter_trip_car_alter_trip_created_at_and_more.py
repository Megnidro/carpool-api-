# Generated by Django 5.0.6 on 2024-06-20 00:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='accounts.carmodel'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profilecustomuser'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='seats',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
