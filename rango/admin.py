from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['category']}),
        ]
    list_display = ('title', 'category', 'url', 'views')
    list_filter = ['category']


admin.site.register(Page, PageAdmin)
admin.site.register(Category)
