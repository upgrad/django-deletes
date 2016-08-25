from .mixins import SoftDeleteManagerMixin, SoftDeleteQuerySetMixin
from django.db import models


class SoftDeleteQuerySet(SoftDeleteQuerySetMixin, models.QuerySet):
    pass


class SoftDeleteManager(SoftDeleteManagerMixin, models.Manager):
    queryset_class = SoftDeleteQuerySet
