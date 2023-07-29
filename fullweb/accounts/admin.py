from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from fullweb.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    list_display = ['username', 'is_staff', 'is_superuser', 'last_login',  'days_out', 'year_out']
    list_filter = ['last_login', 'is_staff']
    ordering = ['last_login', 'pk',]
    fieldsets = (
        ('Credentials', {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),
    )
    list_per_page = 15
    readonly_fields = ['date_joined', 'last_login',]
    search_fields = ['username',]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_photo')
    ordering = ['user',]
    list_filter = ['user',]
    fieldsets = (
        (None, {'fields': ('avatar_photo',)}),
    )
    list_per_page = 15

    def has_add_permission(self, request):
        return False

    def delete_model(self, request, obj):
        obj.avatar_photo = ''
        obj.save()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.avatar_photo = ''
            obj.save()
