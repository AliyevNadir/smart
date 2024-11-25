from django.contrib import admin
from .models import Book, Category
from django.utils.safestring import mark_safe


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'selected_category')
    readonly_fields = ('slug',)

    def selected_category(self, obj):
        html = '<ul>'

        for category in obj.categories.all():
            html += '<li>' + category.name +'</li>'
        return mark_safe(html)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)