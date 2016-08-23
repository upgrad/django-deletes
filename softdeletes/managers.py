from collections import OrderedDict, Counter
from operator import attrgetter

from django.db import models, router, transaction
from django.db.models import signals
from django.contrib import admin
from django.utils import timezone


class DeletableQuerySet(DeletableQuerySetMixin, models.QuerySet):
    pass


class DeletableManager(DeletableManagerMixin, models.Manager):
    queryset_class = DeletableQuerySet
