from .mixins import DeletableManagerMixin, DeletableQuerySetMixin
from django.db import models


class DeletableQuerySet(DeletableQuerySetMixin, models.QuerySet):
    pass


class DeletableManager(DeletableManagerMixin, models.Manager):
    queryset_class = DeletableQuerySet
