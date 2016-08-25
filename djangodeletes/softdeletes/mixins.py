class SoftDeleteQuerySetMixin:

    def delete(self):
        assert self.query.can_filter(), "Cannot use 'limit' or 'offset' with delete."
        for obj in self.all():
            obj.delete()
        self._result_cache = None
    delete.alters_data = True


class SoftDeleteManagerMixin:
    """
    A manager mixin that can be used to created soft deletable managers.
    the manager needs to define queryset_class, default value is DeletableQuerySet
    """

    def __init__(self):
        if not self.queryset_class:
            raise ReferenceError('queryset class not defined in manager') 
        super().__init__()

    def get_queryset(self):

        if self.model:
            return self.queryset_class(self.model, using=self._db).filter(
                deleted=False
            )

    def all_with_deleted(self):
        if self.model:
            return super().get_queryset()

    def only_deleted(self):
        if self.model:
            return super().get_queryset().filter(
                deleted=True
            )

    def filter(self, *args, **kwargs):
        if "pk" in kwargs:
            return self.all_with_deleted().filter(*args, **kwargs)
        return self.get_queryset().filter(*args, **kwargs)

    def get_with_deleted(self, *args, **kwargs):
         return self.all_with_deleted().get(*args, **kwargs)

