from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from connect.models import User, CustomPermission, Role

USER_FIELDS = (
    ("Personal infor", {
     'fields': ('username', 'password1', 'password2', 'first_name', 'last_name')
     }),
    ("Account Confirmation", {
     'fields': ('picture', 'about','email', 'phone_number', 'gender', 'is_confirmed', 'date_of_birth')
     }),
)

# Unregister the Group model from the default admin site
admin.site.unregister(Group)


class CustomPermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'url')
    ordering = ('name',)
admin.site.register(CustomPermission, CustomPermissionAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Role, RoleAdmin)


class MyUserAdmin(UserAdmin):
    model = User
    USER_FIELDS = (
        ('User Information', {
            'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'about', 'picture'),
        }),
        ('Social Login', {
            'fields': ('social_login_id',),
        }),
        ('Permissions', {
            'fields': ('role', 'custom_permissions','is_active', 'is_staff', 'is_superuser', 'is_confirmed'),
        }),
        ('Last Login Details', {
            'fields': ('last_password_update', 'last_login_ip', 'last_login_lat', 'last_login_long'),
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
        }),
    )
    # Specify the fields to include when creating a new user
    add_fieldsets = USER_FIELDS
    fieldsets = USER_FIELDS
    list_display = ('username', 'role', 'email', 'phone_number', 'is_confirmed')

# Register the custom UserAdmin class
admin.site.register(User, MyUserAdmin)
