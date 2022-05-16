# Generated by Django 3.2.13 on 2022-05-15 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0013_auto_20220511_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicine',
            options={'ordering': ('-is_active', 'name'), 'verbose_name': 'Medicine', 'verbose_name_plural': 'Medicines'},
        ),
        migrations.CreateModel(
            name='PatientHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('name', models.CharField(blank=True, max_length=80, null=True, verbose_name='Name')),
                ('social_name', models.CharField(blank=True, max_length=80, null=True, verbose_name='Social Name')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=20, null=True, verbose_name='RG')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('marital_status', models.IntegerField(blank=True, choices=[(1, 'Married'), (2, 'Widowed'), (3, 'Separated'), (4, 'Divorced'), (5, 'Single')], null=True, verbose_name='Marital Status')),
                ('place_of_birth', models.CharField(blank=True, max_length=80, null=True, verbose_name='Place of Birth')),
                ('gender', models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (0, '')], null=True, verbose_name='Gender')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('observation', models.CharField(blank=True, max_length=200, null=True, verbose_name='Observation')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patienthistory_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deactivated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patienthistory_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Deactivated by')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine.patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patienthistory_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Patient History',
                'verbose_name_plural': 'Patient Histories',
                'ordering': ('-id',),
            },
        ),
    ]