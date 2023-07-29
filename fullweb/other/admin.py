from django.contrib import admin

from fullweb.other.models import Other


@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'description', 'amount')
    ordering = ['user', '-amount']
    list_filter = ['amount', 'user', 'date', 'description',]
    fieldsets = (
        (None, {'fields': ('date', 'description', 'amount')}),
    )
    list_per_page = 15

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()