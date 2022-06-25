from django.db import models
from django.utils import timezone
from user.models import CustomUser

from medicine.managers import ActiveManager

MARITAL_STATUS_MARRIED_CHOICE = (1, 'Casado(a)')
MARITAL_STATUS_WIDOWED_CHOICE = (2, 'Viúvo(a)')
MARITAL_STATUS_SEPARATED_CHOICE = (3, 'Separado(a)')
MARITAL_STATUS_DIVORCED_CHOICE = (4, 'Divorciado(a)')
MARITAL_STATUS_SINGLE_CHOICE = (5, 'Solteiro(a)')
MARITAL_STATUS_CHOICES = (
    MARITAL_STATUS_MARRIED_CHOICE,
    MARITAL_STATUS_WIDOWED_CHOICE,
    MARITAL_STATUS_SEPARATED_CHOICE,
    MARITAL_STATUS_DIVORCED_CHOICE,
    MARITAL_STATUS_SINGLE_CHOICE,
)

GENDER_MALE_CHOICE = ('M', 'Masculino')
GENDER_FEMALE_CHOICE = ('F', 'Feminino')
GENDER_OTHER_CHOICE = ('', '')
GENDER_CHOICES = (
    GENDER_OTHER_CHOICE,
    GENDER_MALE_CHOICE,
    GENDER_FEMALE_CHOICE,
)


class BaseModel(models.Model):
    """Define common fields used by other Models by inheritance"""

    created_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Atualizado em',
        auto_now=True
    )

    created_by = models.ForeignKey(
        CustomUser,
        verbose_name='Criado por',
        related_name='%(app_label)s_%(class)s_related_created_by',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    updated_by = models.ForeignKey(
        CustomUser,
        verbose_name='Atualizado por',
        related_name='%(app_label)s_%(class)s_related_updated_by',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    is_active = models.BooleanField(
        verbose_name='Ativo',
        default=True
    )

    deactivated_by = models.ForeignKey(
        CustomUser,
        verbose_name='Inativado por',
        related_name='%(app_label)s_%(class)s_related_deactivated_by',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        """Metadata options"""
        abstract = True


class HistoryBaseModel(models.Model):
    """Define common fields used by other History Models by inheritance"""

    created_at = models.DateTimeField(
        verbose_name='Criado em',
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        verbose_name='Atualizado em',
        null=True,
        blank=True,
    )

    created_by = models.ForeignKey(
        CustomUser,
        verbose_name='Criado por',
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_related_created_by',
        null=True,
        blank=True,
    )

    updated_by = models.ForeignKey(
        CustomUser,
        verbose_name='Atualizado por',
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_related_updated_by',
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        verbose_name='Ativo',
        null=True,
        blank=True,
        default=True,
    )

    deactivated_by = models.ForeignKey(
        CustomUser,
        verbose_name='Inativado por',
        related_name='%(app_label)s_%(class)s_related_deactivated_by',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        """Metadata options"""
        abstract = True


"""
----- Models -----
"""


class Medicine(BaseModel):
    """Medicine Model"""

    name = models.CharField(
        verbose_name='Nome',
        max_length=80,
        null=False,
        blank=False
    )

    description = models.CharField(
        verbose_name='Descrição',
        max_length=100,
        null=False,
        blank=True
    )

    batch = models.CharField(
        verbose_name='Lote',
        max_length=20,
        null=False,
        blank=True
    )

    expiration_date = models.DateField(
        verbose_name='Data de vencimento',
        null=False,
        blank=False
    )

    stock_qty = models.IntegerField(
        verbose_name='Quantidade em estoque',
        null=False,
        blank=False,
        default=0
    )

    objects = models.Manager()
    active_manager = ActiveManager()

    class Meta:
        """Metadata options"""
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering = ('-is_active', 'name',)

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.name


class Patient(BaseModel):
    """Patient Model"""

    name = models.CharField(
        verbose_name='Nome',
        max_length=80,
        null=False,
        blank=False
    )

    social_name = models.CharField(
        verbose_name='Nome Social',
        max_length=80,
        null=False,
        blank=True
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=11,
        null=False,
        blank=False
    )

    rg = models.CharField(
        verbose_name='RG',
        max_length=20,
        null=False,
        blank=False
    )

    birth_date = models.DateField(
        verbose_name='Data de Nascimento',
        null=False,
        blank=False
    )

    marital_status = models.IntegerField(
        verbose_name='Estado Civil',
        choices=MARITAL_STATUS_CHOICES,
        null=False,
        blank=False
    )

    place_of_birth = models.CharField(
        verbose_name='Naturalidade',
        max_length=80,
        null=False,
        blank=True
    )

    gender = models.CharField(
        max_length=2,
        verbose_name='Sexo',
        choices=GENDER_CHOICES,
        null=False,
        blank=True
    )

    phone = models.CharField(
        verbose_name='Telefone',
        max_length=20,
        null=False,
        blank=True
    )

    observation = models.CharField(
        verbose_name='Observação',
        max_length=200,
        null=False,
        blank=True
    )

    objects = models.Manager()
    active_manager = ActiveManager()

    class Meta:
        """Metadata options"""
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ('-is_active', 'name',)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Pacient(name={self.name})'


class NursingProfessional(BaseModel):
    """NursingProfessional Model"""

    name = models.CharField(
        verbose_name='Nome',
        max_length=80,
        null=False,
        blank=False
    )
    coren = models.CharField(
        verbose_name='COREN',
        max_length=20,
        null=False,
        blank=False
    )

    objects = models.Manager()
    active_manager = ActiveManager()

    class Meta:
        """Metadata options"""
        verbose_name = 'Profissional de Enfermagem'
        verbose_name_plural = 'Profissionais de Enfermagem'
        ordering = ('-is_active', 'name',)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'NursingProfessional(name={self.name})'


class MedicalEvaluation(BaseModel):
    """MedicalEvaluation Model"""

    schedule = models.DateTimeField(
        verbose_name='Horário',
        null=False,
        blank=False,
        default=timezone.now
    )

    heart_pressure = models.CharField(
        verbose_name='Pressão Arterial',
        max_length=20,
        null=False,
        blank=False
    )

    glucose = models.CharField(
        verbose_name='Glicose',
        max_length=20,
        null=False,
        blank=False
    )

    observation = models.CharField(
        verbose_name='Observação',
        max_length=200,
        null=False,
        blank=True
    )

    patient = models.ForeignKey(
        verbose_name='Paciente',
        to=Patient,
        on_delete=models.CASCADE,
    )

    nursing_professional = models.ForeignKey(
        verbose_name='Profissional de Enfermagem',
        to=NursingProfessional,
        on_delete=models.CASCADE,
    )

    objects = models.Manager()
    active_manager = ActiveManager()

    class Meta:
        """Metadata options"""
        verbose_name = 'Avaliação Médica'
        verbose_name_plural = 'Avaliações Médicas'
        ordering = ('-is_active', '-schedule',)

    def __str__(self):
        return str(self.schedule)


class Medication(BaseModel):
    """Metadata options"""

    schedule = models.DateTimeField(
        verbose_name='Horário',
        null=False,
        blank=False,
        default=timezone.now
    )

    observation = models.CharField(
        verbose_name='Observação',
        max_length=200,
        null=False,
        blank=True
    )

    medicines = models.ManyToManyField(
        Medicine,
        verbose_name='Medicamentos'
    )

    patient = models.ForeignKey(
        Patient,
        verbose_name='Paciente',
        on_delete=models.CASCADE
    )

    nursing_professional = models.ForeignKey(
        NursingProfessional,
        verbose_name='Profissional de Enfermagem',
        on_delete=models.CASCADE
    )

    objects = models.Manager()
    active_manager = ActiveManager()

    class Meta:
        """Metadata options"""
        verbose_name = 'Medicação'
        verbose_name_plural = 'Medicações'
        ordering = ('-is_active', '-schedule',)

    def __str__(self):
        return str(self.schedule)


"""
----- History Models -----
"""


class MedicineHistory(HistoryBaseModel):
    """Medicine History Model"""

    name = models.CharField(
        verbose_name='Nome',
        max_length=80,
        null=True,
        blank=True
    )

    description = models.CharField(
        verbose_name='Descrição',
        max_length=100,
        null=True,
        blank=True
    )

    batch = models.CharField(
        verbose_name='Lote',
        max_length=20,
        null=True,
        blank=True
    )

    expiration_date = models.DateField(
        verbose_name='Data de vencimento',
        null=True,
        blank=True
    )

    stock_qty = models.IntegerField(
        verbose_name='Quantidade em estoque',
        null=True,
        blank=True,
        default=0
    )

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        """Metadata options"""
        verbose_name = 'Histórico de Medicamento'
        verbose_name_plural = 'Históricos de Medicamento'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'MedicineHistory(name={self.name})'


class PatientHistory(HistoryBaseModel):
    """Patient History Model"""

    name = models.CharField(
        verbose_name='Nome',
        max_length=80,
        null=True,
        blank=True
    )

    social_name = models.CharField(
        verbose_name='Nome Social',
        max_length=80,
        null=True,
        blank=True
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=11,
        null=True,
        blank=True
    )

    rg = models.CharField(
        verbose_name='RG',
        max_length=20,
        null=True,
        blank=True
    )

    birth_date = models.DateField(
        verbose_name='Data de Nascimento',
        null=True,
        blank=True
    )

    marital_status = models.IntegerField(
        verbose_name='Estado Civil',
        choices=MARITAL_STATUS_CHOICES,
        null=True,
        blank=True
    )

    place_of_birth = models.CharField(
        verbose_name='Naturalidade',
        max_length=80,
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=2,
        verbose_name='Sexo',
        choices=GENDER_CHOICES,
        null=True,
        blank=True
    )

    phone = models.CharField(
        verbose_name='Telefone',
        max_length=20,
        null=True,
        blank=True
    )

    observation = models.CharField(
        verbose_name='Observação',
        max_length=200,
        null=True,
        blank=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        """Metadata options"""
        verbose_name = 'Histórico de Paciente'
        verbose_name_plural = 'Históricos de Paciente'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'PatientHistory(name={self.name})'


class NursingProfessionalHistory(HistoryBaseModel):
    """Nursing Professional Model"""

    name = models.CharField(
        verbose_name='Nome',
        max_length=80,
        null=True,
        blank=True
    )

    coren = models.CharField(
        verbose_name='COREN',
        max_length=20,
        null=True,
        blank=True
    )

    nursing_professional = models.ForeignKey(
        NursingProfessional,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        """Metadata options"""
        verbose_name = 'Histórico de Profissional de Enfermagem'
        verbose_name_plural = 'Históricos de Profissional de Enfermagem'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'NursingProfessionalHistory(name={self.name})'


class MedicalEvaluationHistory(HistoryBaseModel):
    """MedicalEvaluationHistory Model"""

    schedule = models.DateTimeField(
        verbose_name='Horário',
        null=True,
        blank=True,
        default=timezone.now
    )

    heart_pressure = models.CharField(
        verbose_name='Pressão Arterial',
        max_length=20,
        null=True,
        blank=True
    )

    glucose = models.CharField(
        verbose_name='Glicose',
        max_length=20,
        null=True,
        blank=True
    )

    observation = models.CharField(
        verbose_name='Observação',
        max_length=200,
        null=True,
        blank=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='medical_evaluations',
        null=True,
        blank=True
    )

    nursing_professional = models.ForeignKey(
        verbose_name='Profissional de Enfermagem',
        to=NursingProfessional,
        on_delete=models.CASCADE
    )

    medical_evaluation = models.ForeignKey(
        verbose_name='Avaliação Médica',
        to=MedicalEvaluation,
        on_delete=models.CASCADE
    )

    class Meta:
        """Metadata options"""
        verbose_name = 'Histórico de Avaliação Médica'
        verbose_name_plural = 'Históricos de Avaliação Médica'
        ordering = ('-id',)

    def __str__(self):
        return str(self.schedule)


class MedicationHistory(HistoryBaseModel):
    """Metadata options"""

    schedule = models.DateTimeField(
        verbose_name='Horário',
        null=True,
        blank=True
    )

    observation = models.CharField(
        verbose_name='Observação',
        max_length=200,
        null=True,
        blank=True
    )

    medicines = models.ManyToManyField(
        to=Medicine,
        verbose_name='Medicamentos'
    )

    patient = models.ForeignKey(
        to=Patient,
        verbose_name='Paciente',
        on_delete=models.CASCADE,
    )

    nursing_professional = models.ForeignKey(
        to=NursingProfessional,
        verbose_name='Profissional de Enfermagem',
        on_delete=models.CASCADE
    )

    medication = models.ForeignKey(
        verbose_name='Medicação',
        to=Medication,
        on_delete=models.CASCADE
    )

    class Meta:
        """Metadata options"""
        verbose_name = 'Histórico de Medicação'
        verbose_name_plural = 'Históricos de Medicação'
        ordering = ('-is_active', '-schedule',)

    def __str__(self):
        return str(self.schedule)
