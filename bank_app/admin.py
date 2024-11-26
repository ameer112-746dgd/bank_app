from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Optionally, if you want to customize the User admin, you can do so like this:
class CustomUserAdmin(UserAdmin):
    # You can customize fields, add list_display, etc. here
    pass

# Unregister the original User admin
admin.site.unregister(User)

# Register the customized User admin
admin.site.register(User, CustomUserAdmin)
