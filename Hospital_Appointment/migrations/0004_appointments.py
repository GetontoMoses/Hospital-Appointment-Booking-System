# Generated by Django 5.0.1 on 2024-01-31 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_Appointment', '0003_patient_rename_staffid_doctor_doctor_staffid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AppointmentDate', models.DateField()),
                ('AppointmentTime', models.TimeField()),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital_Appointment.department')),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital_Appointment.doctor')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital_Appointment.patient')),
            ],
        ),
    ]
