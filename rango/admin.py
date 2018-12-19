from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
class PageInline(admin.TabularInline):
    model = Page
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'views', 'likes']
    inlines = [PageInline]
    list_display = ('name', 'views', 'likes')

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
