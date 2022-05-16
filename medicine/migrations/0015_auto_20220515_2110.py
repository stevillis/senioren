# Generated by Django 3.2.13 on 2022-05-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0014_auto_20220515_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('', '')], max_length=2, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='gender',
            field=models.IntegerField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('', '')], null=True, verbose_name='Gender'),
        ),
    ]