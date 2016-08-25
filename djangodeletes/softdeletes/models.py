from collections import OrderedDict, Counter
from operator import attrgetter

from django.db import models, router, transaction
from django.db.models import signals
from django.utils import timezone


class SoftDeletable(models.Model):
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        abstract = True

    def sort(self):
        sorted_models = []
        concrete_models = set()
        models = list(self.collector.data)
        while len(sorted_models) < len(models):
            found = False
            for model in models:
                if model in sorted_models:
                    continue
                dependencies = self.collector.dependencies.get(model._meta.concrete_model)
                if not (dependencies and dependencies.difference(concrete_models)):
                    sorted_models.append(model)
                    concrete_models.add(model._meta.concrete_model)
                    found = True
            if not found:
                return
        self.collector.data = OrderedDict((model, self.collector.data[model])
                                  for model in sorted_models)

    def delete(self, using=None, keep_parents=False):
        using = using or router.db_for_write(self.__class__, instance=self)
        deleted_counter = Counter()
        assert self._get_pk_val() is not None, (
                "{0} object can't be deleted because its {1} attribute is set to None.".format(self._meta.object_name, self._meta.pk.attname))

        self.collector = models.deletion.Collector(using=using) 
        self.collector.collect([self], keep_parents=keep_parents)

        # sort instance collections
        for model, instances in self.collector.data.items():
            instances_to_delete = sorted(instances, key=attrgetter("pk"))

        self.sort()

        with transaction.atomic(using=using, savepoint=False):
            # send pre_delete signals
            for model, obj in self.collector.instances_with_model():
                if not model._meta.auto_created:
                    signals.pre_delete.send(sender=model, instance=obj, using=using)

            # fast deletes
            for qs in self.collector.fast_deletes:
                # TODO make sure the queryset delete has been made a soft delete
                for qs_instance in qs:
                    deleted_counter.update([qs_instance._meta.model_name])
                    qs_instance._delete()

            # reverse instance collections
            #for instances in self.collector.data.items():
            #    instances.reverse()

            for model, instances in self.collector.data.items():
                for instance in instances:
                    deleted_counter.update([instance._meta.model_name])
                    instance._delete()
                    if not model._meta.auto_created:
                        signals.post_delete.send(
                            sender=model, instance=obj, using=using
                        )

        # update collected instances
        for model, instances_for_fieldvalues in self.collector.field_updates.items():
            for (field, value), instances in instances_for_fieldvalues.items():
                for obj in instances:
                    setattr(obj, field.attname, value)

        for model, instances in self.collector.data.items():
            for instance in instances:
                setattr(instance, model._meta.pk.attname, None)
        return sum(deleted_counter.values()), dict(deleted_counter)

    def _delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        # print('Deleting model {0} object with id {1}'.format(self._meta.model_name, self.id))
        self.save()
