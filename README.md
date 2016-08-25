## Soft Deletes for Django (in beta)
Supported Django versions >= 1.8
Supported Python versions >= 3.3

### Installation Instructions
1. pip install djangodeletes 
2. softdeletes will be available to import as ```from djangodeletes.softdeletes.models import SoftDeletable```

### Usage
1. Use Deletable class on the left most in the inhertance chain of the model. 
2. Use objects = DeletableManager.from_queryset(DeletableQuerySet)()
3. If you want to use a custom manager or a custom Queryset, make sure your custom manager inherits from DeletableManagerMixin and your custom QuerySet inherits from Deletable QuerySetMixin


### Caution
All cascading delete models should be made deletable, otherwise cascading delete would do a real delete to the foreignkey related models.



### Reporting a bug / Issue
Issues can be reported on https://github.com/upgrad/django-deletes/issues.

### Contributing
Contributions welcome for the issues reported on issue tracker. 

### Terminologies

3. soft deletes (logical deletes) - Deleting a record in a table by marking a boolean column (usually `deleted`, `removed`) as True. While fetching the records consider only those records which have this boolean set as False
2. cascading instances - Instances which should get deleted when the django's default cascading method is used in physical deletion. Ideally a soft delete should also follow up with these instances or records and soft delete them. 
1. live instances - record objects which are not soft deleted. 
5. SoftDeletable model - A model which has Soft Delete activated
