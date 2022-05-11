from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from user.models import CustomUser


class BaseModel(models.Model):
    """Define common fields used by other Models by inheritance"""
    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated at'),
        auto_now=True
    )
    created_by = models.ForeignKey(
        CustomUser,
        verbose_name=_('Created by'),
        related_name='%(app_label)s_%(class)s_related_created_by',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        CustomUser,
        verbose_name=_('Updated by'),
        related_name='%(app_label)s_%(class)s_related_updated_by',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=True
    )

    class Meta:
        """Metadata options"""
        abstract = True


class HistoryBaseModel(models.Model):
    """Define common fields used by other History Models by inheritance"""
    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated at'),
        null=False,
        blank=False,
    )
    created_by = models.ForeignKey(
        CustomUser,
        verbose_name=_('Created by'),
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_related_created_by',
        null=False,
        blank=False,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        verbose_name=_('Updated by'),
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_related_updated_by',
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        null=False,
        blank=False,
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
        verbose_name=_('Name'),
        max_length=80,
        null=False,
        blank=False
    )
    description = models.CharField(
        verbose_name=_('Description'),
        max_length=100,
        null=False,
        blank=True
    )
    batch = models.CharField(
        verbose_name=_('Batch'),
        max_length=20,
        null=False,
        blank=True
    )
    expiration_date = models.DateField(
        verbose_name=_('Expiration date'),
        null=False,
        blank=False
    )
    stock_qty = models.IntegerField(
        verbose_name=_('Stock quantity'),
        null=False,
        blank=False,
        default=0
    )

    class Meta:
        """Metadata options"""
        verbose_name = _('Medicine')
        verbose_name_plural = _('Medicines')
        ordering = ('name',)

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.name


class Patient(BaseModel):
    """Patient Model"""
    MARITAL_STATUS_MARRIED_CHOICE = (1, _('Married'))
    MARITAL_STATUS_WIDOWED_CHOICE = (2, _('Widowed'))
    MARITAL_STATUS_SEPARATED_CHOICE = (3, _('Separated'))
    MARITAL_STATUS_DIVORCED_CHOICE = (4, _('Divorced'))
    MARITAL_STATUS_SINGLE_CHOICE = (5, _('Single'))
    MARITAL_STATUS_CHOICES = (
        MARITAL_STATUS_MARRIED_CHOICE,
        MARITAL_STATUS_WIDOWED_CHOICE,
        MARITAL_STATUS_SEPARATED_CHOICE,
        MARITAL_STATUS_DIVORCED_CHOICE,
        MARITAL_STATUS_SINGLE_CHOICE,
    )

    GENDER_MALE_CHOICE = (1, _('Male'))
    GENDER_FEMALE_CHOICE = (2, _('Female'))
    GENDER_OTHER_CHOICE = (0, '')
    GENDER_CHOICES = (
        GENDER_MALE_CHOICE,
        GENDER_FEMALE_CHOICE,
        GENDER_OTHER_CHOICE,
    )

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=80,
        null=False,
        blank=False
    )
    social_name = models.CharField(
        verbose_name=_('Social Name'),
        max_length=80,
        null=False,
        blank=True
    )
    cpf = models.CharField(
        verbose_name=_('CPF'),
        max_length=11,
        null=False,
        blank=False
    )
    rg = models.CharField(
        verbose_name=_('RG'),
        max_length=20,
        null=False,
        blank=False
    )
    birth_date = models.DateField(
        verbose_name=_('Birth Date'),
        null=False,
        blank=False
    )
    marital_status = models.IntegerField(
        verbose_name=_('Marital Status'),
        choices=MARITAL_STATUS_CHOICES,
        null=False,
        blank=False
    )
    place_of_birth = models.CharField(
        verbose_name=_('Place of Birth'),
        max_length=80,
        null=False,
        blank=True
    )
    gender = models.IntegerField(
        verbose_name=_('Gender'),
        choices=GENDER_CHOICES,
        null=False,
        blank=True
    )
    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=20,
        null=False,
        blank=True
    )
    observation = models.CharField(
        verbose_name=_('Observation'),
        max_length=200,
        null=False,
        blank=True
    )

    class Meta:
        """Metadata options"""
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')
        ordering = ('name',)

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.name


class NursingProfessional(BaseModel):
    """NursingProfessional Model"""
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=80,
        null=False,
        blank=False
    )
    coren = models.CharField(
        verbose_name=_('COREN'),
        max_length=20,
        null=False,
        blank=False
    )

    class Meta:
        """Metadata options"""
        verbose_name = _('Nursing Professional')
        verbose_name_plural = _('Nursing Professionals')
        ordering = ('name',)

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.name


class MedicalEvaluation(BaseModel):
    """MedicalEvaluation Model"""
    schedule = models.DateTimeField(
        verbose_name=_('Schedule'),
        null=False,
        blank=False,
        default=timezone.now
    )
    heart_pressure = models.CharField(
        verbose_name=_('Heart pressure'),
        max_length=20,
        null=False,
        blank=False)
    glucose = models.CharField(
        verbose_name=_('Glucose'),
        max_length=20,
        null=False,
        blank=False)
    observation = models.CharField(
        verbose_name=_('Observation'),
        max_length=200,
        null=False,
        blank=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='medical_evaluations',
        null=False,
        blank=False
    )
    nursing_professional = models.ForeignKey(
        verbose_name=_('Nursing Professional'),
        to=NursingProfessional,
        on_delete=models.CASCADE
    )

    class Meta:
        """Metadata options"""
        verbose_name = _('Medical Evaluation')
        verbose_name_plural = _('Medical Evaluations')
        ordering = ('-schedule',)

    def __str__(self):
        return str(self.schedule)


class Medication(BaseModel):
    """Metadata options"""
    schedule = models.DateTimeField(
        verbose_name=_('Schedule'),
        null=False,
        blank=False,
        default=timezone.now
    )
    observation = models.CharField(
        verbose_name=_('Observation'),
        max_length=200,
        null=False,
        blank=True
    )

    medicine = models.ManyToManyField(
        Medicine,
        verbose_name=_('Medicines')
    )
    patient = models.ForeignKey(
        Patient,
        verbose_name=_('Patient'),
        on_delete=models.CASCADE
    )
    nursing_professional = models.ForeignKey(
        NursingProfessional,
        verbose_name=_('Nursing Professional'),
        on_delete=models.CASCADE
    )

    class Meta:
        """Metadata options"""
        verbose_name = _('Medication')
        verbose_name_plural = _('Medications')

    def __str__(self):
        return str(self.schedule)


"""
----- History Models -----
"""


class MedicineHistory(HistoryBaseModel):
    """Medicine Model"""
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=80,
        null=True,
        blank=True
    )
    description = models.CharField(
        verbose_name=_('Description'),
        max_length=100,
        null=True,
        blank=True
    )
    batch = models.CharField(
        verbose_name=_('Batch'),
        max_length=20,
        null=True,
        blank=True
    )
    expiration_date = models.DateField(
        verbose_name=_('Expiration date'),
        null=True,
        blank=True
    )
    stock_qty = models.IntegerField(
        verbose_name=_('Stock quantity'),
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
        verbose_name = _('Medicine History')
        verbose_name_plural = _('Medicine Histories')
        ordering = ('-id',)

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.name
