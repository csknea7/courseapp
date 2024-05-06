from django.contrib import admin
from .models import Category, Destination


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("field",)
    ordering = ("field",)


# Register your models here.

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "description", "category",)
    list_editable = ("title", "description",)
    ordering = ("name",)
