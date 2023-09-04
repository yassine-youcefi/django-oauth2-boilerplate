from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from connect.models import User

ADDITIONAL_USER_FIELDS = (
    ("Account Confirmation", {
     'fields': ('picture', 'about', 'phone_number', 'is_confirmed', 'gender', 'date_of_birth')
     }),
)


class MyUserAdmin(UserAdmin):
    model = User
    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS
    list_display = ('username', 'email', 'phone_number',
                    'first_name', 'last_name', 'is_confirmed')


admin.site.register(User, MyUserAdmin)


