from django.contrib import admin


class DeletableModelAdmin(admin.ModelAdmin):
    """
    Base class for admin / staff interface
    """
    list_display = ("id", "__str__", "deleted")
    list_display_filter = ("deleted", )

    def get_queryset(self, request):
        qs = self.model._default_manager.all_with_deleted()
        if self.ordering:
            qs = qs.order_by(*ordering)
        return qs
