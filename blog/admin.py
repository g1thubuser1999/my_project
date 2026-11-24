from django.contrib import admin
from .models import BannerModel, Category, AboutModel

admin.site.register(BannerModel)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'sub_title')
    search_fields = ('name', 'title')


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
