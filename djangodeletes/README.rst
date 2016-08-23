Soft Deletes for Django.
------------------------

Installation Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

#. pip install django-deletes # Doesnt work yet, clone the repo.
#. Add ‘softdeletes’ to INSTALLED\_APPS in settings

Usage
~~~~~

#. Use Deletable class on the left most in the inhertance chain of the
   model.
#. Use objects = DeletableManager.from\_queryset(DeletableQuerySet)()
#. If you want to use a custom manager or a custom Queryset, make sure
   your custom manager inherits from DeletableManagerMixin and your
   custom QuerySet inherits from Deletable QuerySetMixin

Caution
~~~~~~~

All cascading delete models should be made deletable, otherwise
cascading delete would do a real delete to the foreignkey related
models.
