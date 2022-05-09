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


class MedicalEvaluation(BaseModel):
    schedule = models.DateTimeField(_('Schedule'), null=False, blank=False, default=timezone.now)
    heart_pressure = models.CharField(_('Heart pressure'), max_length=20, null=False, blank=False)
    glucose = models.CharField(_('Glucose'), max_length=20, null=False, blank=False)
    observation = models.CharField(_('Observation'), max_length=200, null=False, blank=True)

    class Meta:
        verbose_name = _('Medical Evaluation')
        verbose_name_plural = _('Medical Evaluations')
        ordering = ('-schedule',)

    def __str__(self):
        return str(self.schedule)
