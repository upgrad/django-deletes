#### Basic Usage
```
from djangodeletes.softdelete import SoftDeletable, SoftDeletaManager, SoftDeleteQuerySet


class MyModel(SoftDeletable, models.Model):
    ...
    ...
    ...

    objects = SoftDeletaManager.from_queryset(SoftDeleteQuerySet)()

    def __str__(self):
        ...
```


#### To use a custom queryset with your soft deletable model

```
# Create a custom  queryset that inherits from SoftDeleteQuerySetMixin

class CustomQuerySet(SoftDeleteQuerySetMixin, models.QuerySet):
    
    def custom_queryset_method(self):
        ....
        ...

# use this queryset in your model

objects = SoftDeletaManager.from_queryset(CustomQuerySet)()

```


#### To use a custom manager with your soft deletable model

```
# Create a custom manager that inherits from SoftDeleteQuerySetMixin
# and set the queryset_class as SoftDeleteQuerySet

class CustomModelManager(SoftDeleteManagerMixin, models.Manager):
	queryset_class = SoftDeleteQuerySet
    
    def custom_manager_method(self):
        ....
        ...

# use this manager in your model

objects = CustomModelManager.from_queryset(SoftDeleteQuerySet)()

```


#### To use a custom manager and custom queryset both with your model


```
class CustomQuerySet(SoftDeleteQuerySetMixin, models.QuerySet):
    
    def custom_queryset_method(self):
        ....
        ...

class CustomModelManager(SoftDeleteManagerMixin, models.Manager):
	queryset_class = SoftDeleteQuerySet
    
    def custom_manager_method(self):
        ....
        ...

# use this manager in your model

objects = CustomModelManager.from_queryset(CustomQuerySet)()

```
1. Use Deletable class on the left most in the inhertance chain of the model. 
2. Use objects = DeletableManager.from_queryset(DeletableQuerySet)()
3. If you want to use a custom manager or a custom Queryset, make sure your custom manager inherits from DeletableManagerMixin and your custom QuerySet inherits from Deletable QuerySetMixin

