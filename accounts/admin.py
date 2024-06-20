from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ProfileCustomUser, CarModel, Reclaim, Address


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class ProfileCustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'role', 'category')
    list_filter = ('role', 'category')
    search_fields = ('user__email', 'phone_number')

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'owner')
    list_filter = ('make', 'year')
    search_fields = ('make', 'model', 'licence_number')

class ReclaimAdmin(admin.ModelAdmin):
    list_display = ('owner', 'date', 'reason')
    list_filter = ('date',)
    search_fields = ('owner__user__email', 'reason')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'city', 'country', 'author')
    list_filter = ('city', 'country', 'type_of_address')
    search_fields = ('position_name', 'street', 'city')

# Enregistrement des modèles avec leurs classes Admin personnalisées
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ProfileCustomUser, ProfileCustomUserAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Reclaim, ReclaimAdmin)
admin.site.register(Address, AddressAdmin)