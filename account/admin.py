from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.forms import UserAdminCreationForm, UserAdminChangeForm


User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('email', 'name', 'surname', 'is_active', 'is_superuser',
                    'activation_code', 'slug', 'password_reset_code', )
    list_filter = ('is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'surname', 'password', 'pp', 'password_reset_code')}),
        # ('Full name', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'surname', 'password1', 'password2')}
         ),
    )
    readonly_fields = ('created_at',)
    search_fields = ('email', 'name', 'surname')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
