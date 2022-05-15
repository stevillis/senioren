from django.db import models


class ActiveManager(models.Manager):
    """Manager to filter only active records."""

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
