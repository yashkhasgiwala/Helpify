from django.contrib import admin
from cuser.admin import UserAdmin
from .models import HUser, Report
from django.contrib.auth.forms import UserCreationForm


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Additional Info',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'phone',
                    'reg_plate1',
                    'contact_phone1'
                ),
            },
        ),
    )

admin.site.register(HUser, CustomUserAdmin)
admin.site.register(Report)