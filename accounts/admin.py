from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import CustomUser, CarModel, Notification, Reclaim, Address, ProfileCustomUser


@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    icon = "user"


@admin.register(ProfileCustomUser)
class ProfileCustomUserAdmin(ModelAdmin):
    list_display = ('user', 'role', 'phone_number', 'birth_date', 'category')
    list_filter = ('role', 'category', 'genre')
    search_fields = ('user__email', 'phone_number', 'num_permis')
    raw_id_fields = ('user',)
    fieldsets = (
        ('User Info', {'fields': ('user', 'avatar', 'birth_date', 'genre')}),
        ('Driver Info', {'fields': ('num_permis', 'category', 'date_delivrance', 'date_expiration')}),
        ('Role', {'fields': ('role',)}),
    )
    icon = "id-card"


@admin.register(CarModel)
class CarModelAdmin(ModelAdmin):
    list_display = ('make', 'model', 'year', 'color', 'licence_number', 'owner')
    list_filter = ('make', 'year')
    search_fields = ('make', 'model', 'licence_number', 'owner__user__email')
    raw_id_fields = ('owner',)
    icon = "car"


@admin.register(Notification)
class NotificationAdmin(ModelAdmin):
    # Comme le modèle Notification est vide, vous pouvez le personnaliser
    # une fois que vous aurez ajouté des champs
    pass


@admin.register(Reclaim)
class ReclaimAdmin(ModelAdmin):
    list_display = ('owner', 'date', 'reason')
    list_filter = ('date',)
    search_fields = ('owner__user__email', 'reason')
    raw_id_fields = ('owner',)
    date_hierarchy = 'date'
    icon = "file-text"


@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = ('position_name', 'city', 'country', 'type_of_address', 'author')
    list_filter = ('country', 'type_of_address')
    search_fields = ('position_name', 'city', 'street', 'author__user__email')
    raw_id_fields = ('author',)
    fieldsets = (
        ('Location', {'fields': ('position_name', 'number', 'street', 'city', 'region', 'country', 'postal_code')}),
        ('Additional Info', {'fields': ('google_maps', 'type_of_address', 'author')}),
    )
    icon = "map-pin"
