# Generated by Django 3.2.13 on 2022-05-11 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0012_medicinehistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalevaluation',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicalevaluation_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Deactivated by'),
        ),
        migrations.AddField(
            model_name='medication',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medication_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Deactivated by'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicine_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Deactivated by'),
        ),
        migrations.AddField(
            model_name='medicinehistory',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicinehistory_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Deactivated by'),
        ),
        migrations.AddField(
            model_name='nursingprofessional',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_nursingprofessional_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Deactivated by'),
        ),
        migrations.AddField(
            model_name='patient',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patient_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Deactivated by'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicalevaluation_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medication_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicine_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicinehistory_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicinehistory_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='nursingprofessional',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_nursingprofessional_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patient_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
    ]