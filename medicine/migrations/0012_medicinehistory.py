# Generated by Django 3.2.13 on 2022-05-11 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0011_auto_20220510_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Created at')),
                ('updated_at', models.DateTimeField(verbose_name='Updated at')),
                ('is_active', models.BooleanField(verbose_name='Active')),
                ('name', models.CharField(blank=True, max_length=80, null=True, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('batch', models.CharField(blank=True, max_length=20, null=True, verbose_name='Batch')),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='Expiration date')),
                ('stock_qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Stock quantity')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicinehistory_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicinehistory_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Medicine History',
                'verbose_name_plural': 'Medicine Histories',
                'ordering': ('-id',),
            },
        ),
    ]