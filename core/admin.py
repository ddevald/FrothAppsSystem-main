from django.contrib import admin
from core.models import ProjectType, User, Project, Appointment, Milestone
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username']
    list_filter = ('is_active',)
    fieldsets = (
        (_('Personal Info'), {
            'fields': ('email', 'password', 'avatar', 'username',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        (_('Important Dates'), {
            'fields': ('last_login',)
        })
    )
    add_fieldsets = (
        (_('Personal Info'), {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Project)
admin.site.register(Appointment)
admin.site.register(ProjectType)
admin.site.register(Milestone)
