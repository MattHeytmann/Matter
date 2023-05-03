from django.contrib import admin
from .models import Customer

@admin.action(description='make active')
def make_active(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.action(description='make unactive')
def make_unactive(modeladmin, request, queryset):
    queryset.update(active=False)


@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")
    actions = [make_active, make_unactive]


admin.site.site_header = "MATTER"
