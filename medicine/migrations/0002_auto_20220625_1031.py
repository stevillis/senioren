# Generated by Django 3.2.13 on 2022-06-25 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicalevaluation',
            options={'ordering': ('-is_active', '-schedule'), 'verbose_name': 'Avaliação Médica', 'verbose_name_plural': 'Avaliações Médicas'},
        ),
        migrations.AlterModelOptions(
            name='medicalevaluationhistory',
            options={'ordering': ('-id',), 'verbose_name': 'Histórico de Avaliação Médica', 'verbose_name_plural': 'Históricos de Avaliação Médica'},
        ),
        migrations.AlterModelOptions(
            name='medication',
            options={'ordering': ('-is_active', '-schedule'), 'verbose_name': 'Medicação', 'verbose_name_plural': 'Medicações'},
        ),
        migrations.AlterModelOptions(
            name='medicationhistory',
            options={'ordering': ('-is_active', '-schedule'), 'verbose_name': 'Histórico de Medicação', 'verbose_name_plural': 'Históricos de Medicação'},
        ),
        migrations.AlterModelOptions(
            name='medicine',
            options={'ordering': ('-is_active', 'name'), 'verbose_name': 'Medicamento', 'verbose_name_plural': 'Medicamentos'},
        ),
        migrations.AlterModelOptions(
            name='medicinehistory',
            options={'ordering': ('-id',), 'verbose_name': 'Histórico de Medicamento', 'verbose_name_plural': 'Históricos de Medicamento'},
        ),
        migrations.AlterModelOptions(
            name='nursingprofessional',
            options={'ordering': ('-is_active', 'name'), 'verbose_name': 'Profissional de Enfermagem', 'verbose_name_plural': 'Profissionais de Enfermagem'},
        ),
        migrations.AlterModelOptions(
            name='nursingprofessionalhistory',
            options={'ordering': ('-id',), 'verbose_name': 'Histórico de Profissional de Enfermagem', 'verbose_name_plural': 'Históricos de Profissional de Enfermagem'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ('-is_active', 'name'), 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AlterModelOptions(
            name='patienthistory',
            options={'ordering': ('-id',), 'verbose_name': 'Histórico de Paciente', 'verbose_name_plural': 'Históricos de Paciente'},
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicalevaluation_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicalevaluation_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Inativado por'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='glucose',
            field=models.CharField(max_length=20, verbose_name='Glicose'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='heart_pressure',
            field=models.CharField(max_length=20, verbose_name='Pressão Arterial'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='nursing_professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.nursingprofessional', verbose_name='Profissional de Enfermagem'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='observation',
            field=models.CharField(blank=True, max_length=200, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.patient', verbose_name='Paciente'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='schedule',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Horário'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='medicalevaluation',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicalevaluation_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='created_at',
            field=models.DateTimeField(verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicalevaluationhistory_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicalevaluationhistory_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Inativado por'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='glucose',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Glicose'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='heart_pressure',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Pressão Arterial'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='medical_evaluation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medicalevaluation', verbose_name='Avaliação Médica'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='nursing_professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.nursingprofessional', verbose_name='Profissional de Enfermagem'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='observation',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='schedule',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Horário'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='medicalevaluationhistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicalevaluationhistory_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medication_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medication_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Inativado por'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='medicines',
            field=models.ManyToManyField(to='medicine.Medicine', verbose_name='Medicamentos'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='nursing_professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.nursingprofessional', verbose_name='Profissional de Enfermagem'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='observation',
            field=models.CharField(blank=True, max_length=200, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.patient', verbose_name='Paciente'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='schedule',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Horário'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medication_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='created_at',
            field=models.DateTimeField(verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicationhistory_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicationhistory_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Inativado por'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='medication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medication', verbose_name='Medicação'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='medicines',
            field=models.ManyToManyField(to='medicine.Medicine', verbose_name='Medicamentos'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='nursing_professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.nursingprofessional', verbose_name='Profissional de Enfermagem'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='observation',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.patient', verbose_name='Paciente'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='schedule',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Horário'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='medicationhistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicationhistory_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='batch',
            field=models.CharField(blank=True, max_length=20, verbose_name='Lote'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicine_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicine_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Inativado por'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='description',
            field=models.CharField(blank=True, max_length=100, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='expiration_date',
            field=models.DateField(verbose_name='Data de vencimento'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='stock_qty',
            field=models.IntegerField(default=0, verbose_name='Quantidade em estoque'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicine_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='batch',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Lote'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='created_at',
            field=models.DateTimeField(verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicinehistory_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicinehistory_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Inativado por'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de vencimento'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='stock_qty',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade em estoque'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='medicinehistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_medicinehistory_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='nursingprofessional',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='nursingprofessional',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_nursingprofessional_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='nursingprofessional',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_nursingprofessional_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Inativado por'),
        ),
        migrations.AlterField(
            model_name='nursingprofessional',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='nursingprofessional',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='nursingprofessional',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='nursingprofessional',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_nursingprofessional_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='nursingprofessionalhistory',
            name='created_at',
            field=models.DateTimeField(verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='nursingprofessionalhistory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_nursingprofessionalhistory_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='nursingprofessionalhistory',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_nursingprofessionalhistory_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Inativado por'),
        ),
        migrations.AlterField(
            model_name='nursingprofessionalhistory',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='nursingprofessionalhistory',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='nursingprofessionalhistory',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='nursingprofessionalhistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_nursingprofessionalhistory_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patient_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patient_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Inativado por'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('', ''), ('M', 'Masculino'), ('F', 'Feminino')], max_length=2, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.IntegerField(choices=[(1, 'Casado(a)'), (2, 'Viúvo(a)'), (3, 'Separado(a)'), (4, 'Divorciado(a)'), (5, 'Solteiro(a)')], verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='observation',
            field=models.CharField(blank=True, max_length=200, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=80, verbose_name='Naturalidade'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='social_name',
            field=models.CharField(blank=True, max_length=80, verbose_name='Nome Social'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patient_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='created_at',
            field=models.DateTimeField(verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patienthistory_related_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='deactivated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patienthistory_related_deactivated_by', to=settings.AUTH_USER_MODEL, verbose_name='Inativado por'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='gender',
            field=models.CharField(blank=True, choices=[('', ''), ('M', 'Masculino'), ('F', 'Feminino')], max_length=2, null=True, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='marital_status',
            field=models.IntegerField(blank=True, choices=[(1, 'Casado(a)'), (2, 'Viúvo(a)'), (3, 'Separado(a)'), (4, 'Divorciado(a)'), (5, 'Solteiro(a)')], null=True, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='observation',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Naturalidade'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='social_name',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Nome Social'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine_patienthistory_related_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
    ]
