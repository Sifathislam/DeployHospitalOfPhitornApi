# Generated by Django 4.2.7 on 2024-01-10 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_review'),
        ('appointment', '0002_rename_appointmentd_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime'),
        ),
    ]
