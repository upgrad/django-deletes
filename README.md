## Soft Deletes for Django (in beta)

Simplest soft delete library for Django.


Supported Django versions >= 1.8
Supported Python versions >= 3.3

### Installation Instructions
1. pip install djangodeletes


### Basic Usage

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

### Background

### APIs

1. Delete - All model deletes and queryset deletes will result in soft delete. Default option is Cascade. All related objects will also get softdeleted. This behaviour exactly maps with what happens with real delete

2. Fetching / filtering a queryset - Soft deleted objects will remain hidden from all queries.

2. Getting single object - if the specific object is soft deleted, it would raise normal exception of ObjectDoesNotExist

3. Fetching deleted objects - Following options are available.

    a. Model.objects.get_with_deleted(pk=12)  # similar to get operation ignores softdeletes

    b. Model.objects.only_deleted()  - All the deleted objects

    c. Model.objects.all_with_deleted() - A queryset including deleted objects

    d. Model.objects.filter(pk=55) - Only this filter query ignores the deleted flag and returns then object even if that is deleted

    d. Model.objects.filter(pk=55) - Only this filter query ignores the deleted flag and returns then object even if that is deleted

* For Advanced usage, look at docs/usage.md

4. Restore an object
    a. something.restore() - A model method which restores the object.

    b. something.full_restore() - A model method which restores the object and all other related objects which were deleted along with that operation.

5. Delete an object permanently
    a. someobject.hard_delete()


### Caution
All cascading delete models should be made deletable, otherwise cascading delete would do a real delete to the foreignkey related models.

### Reporting a bug / Issue
Issues can be reported on https://github.com/upgrad/django-deletes/issues.

### Contributing
Contributions welcome. For sending patch requests or fixes, send a pull request.

### Terminologies

3. soft deletes (logical deletes) - Deleting a record in a table by marking a boolean column (usually `deleted`, `removed`) as True. While fetching the records consider only those records which have this boolean set as False
2. cascading instances - Instances which should get deleted when the django's default cascading method is used in physical deletion. Ideally a soft delete should also follow up with these instances or records and soft delete them.
1. live instances - record objects which are not soft deleted.
5. SoftDeletable model - A model which has Soft Delete activated
