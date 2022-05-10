from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        abstract = True


class Medicine(BaseModel):
    name = models.CharField(_('Name'), max_length=80, null=False, blank=False)
    description = models.CharField(_('Description'), max_length=100, null=False, blank=True)
    batch = models.CharField(_('Batch'), max_length=20, null=False, blank=True)
    expiration_date = models.DateField(_('Expiration date'), null=False, blank=False)
    stock_qty = models.IntegerField(_('Stock quantity'), null=False, blank=False, default=0)

    class Meta:
        verbose_name = _('Medicine')
        verbose_name_plural = _('Medicines')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Patient(BaseModel):
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

    name = models.CharField(_('Name'), max_length=80, null=False, blank=False)
    social_name = models.CharField(_('Social Name'), max_length=80, null=False, blank=True)
    cpf = models.CharField(_('CPF'), max_length=11, null=False, blank=False)
    rg = models.CharField(_('RG'), max_length=20, null=False, blank=False)
    birth_date = models.DateField(_('Birth Date'), null=False, blank=False)
    marital_status = models.IntegerField(_('Marital Status'), choices=MARITAL_STATUS_CHOICES, null=False,
                                         blank=False)
    place_of_birth = models.CharField(_('Place of Birth'), max_length=80, null=False, blank=True)
    gender = models.IntegerField(_('Gender'), choices=GENDER_CHOICES, null=False, blank=True)
    phone = models.CharField(_('Phone'), max_length=20, null=False, blank=True)
    observation = models.CharField(_('Observation'), max_length=200, null=False, blank=True)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')
        ordering = ('name',)

    def __str__(self):
        return self.name


class MedicalEvaluation(BaseModel):
    schedule = models.DateTimeField(_('Schedule'), null=False, blank=False, default=timezone.now)
    heart_pressure = models.CharField(_('Heart pressure'), max_length=20, null=False, blank=False)
    glucose = models.CharField(_('Glucose'), max_length=20, null=False, blank=False)
    observation = models.CharField(_('Observation'), max_length=200, null=False, blank=True)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_evaluations', null=False,
                                blank=False)

    class Meta:
        verbose_name = _('Medical Evaluation')
        verbose_name_plural = _('Medical Evaluations')
        ordering = ('-schedule',)

    def __str__(self):
        return str(self.schedule)


class NursingProfessional(BaseModel):
    name = models.CharField(_('Name'), max_length=80, null=False, blank=False)
    coren = models.CharField(_('COREN'), max_length=20, null=False, blank=False)

    class Meta:
        verbose_name = _('Nursing Professional')
        verbose_name_plural = _('Nursing Professionals')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Medication(BaseModel):
    schedule = models.DateTimeField(_('Schedule'), null=False, blank=False, default=timezone.now)
    observation = models.CharField(_('Observation'), max_length=200, null=False, blank=True)

    medicine = models.ManyToManyField(verbose_name=_('Medicines'), to=Medicine)
    patient = models.ForeignKey(verbose_name=_('Patient'), to=Patient, on_delete=models.CASCADE)
    nursing_professional = models.ForeignKey(verbose_name=_('Nursing Professional'), to=NursingProfessional,
                                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Medication')
        verbose_name_plural = _('Medications')

    def __str__(self):
        return str(self.schedule)
