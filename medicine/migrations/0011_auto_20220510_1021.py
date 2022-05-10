# Generated by Django 3.2.13 on 2022-05-10 14:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0010_auto_20220510_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalevaluation',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='medicine_medicalevaluation_related_created_by', to='user.customuser',
                                    verbose_name='Created by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicalevaluation',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='medicine_medicalevaluation_related_updated_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='medication',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='medicine_medication_related_created_by', to='user.customuser',
                                    verbose_name='Created by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medication',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='medicine_medication_related_updated_by', to=settings.AUTH_USER_MODEL,
                                    verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='medicine_medicine_related_created_by', to='user.customuser',
                                    verbose_name='Created by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='medicine_medicine_related_updated_by', to=settings.AUTH_USER_MODEL,
                                    verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='nursingprofessional',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='medicine_nursingprofessional_related_created_by',
                                    to='user.customuser', verbose_name='Created by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nursingprofessional',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='medicine_nursingprofessional_related_updated_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='patient',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='medicine_patient_related_created_by', to='user.customuser',
                                    verbose_name='Created by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='medicine_patient_related_updated_by', to=settings.AUTH_USER_MODEL,
                                    verbose_name='Updated by'),
        ),
    ]