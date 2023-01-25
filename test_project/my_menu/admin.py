from django.contrib import admin
from .models import Menu
# Register your models here.


class MenuInline(admin.StackedInline):
    model = Menu.children.through


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_root', 'display_children')
    fields = ['name', 'url', 'is_root', 'children']
    # inlines = [MenuInline]
