from django.contrib import admin
from products.models import CategoryModel, BrandModel, ColorModel, SizeModel, ProductModel
from modeltranslation.admin import TranslationAdmin


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(BrandModel)
class BrandModelAdmin(MyTranslationAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(ColorModel)
class ColorModelAdmin(MyTranslationAdmin):
    list_display = ['color']
    search_fields = ['color']
    list_filter = ['color']


@admin.register(SizeModel)
class SizeModelAdmin(MyTranslationAdmin):
    list_display = ['size']
    search_fields = ['size']
    list_filter = ['size']


@admin.register(ProductModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['name', 'category', 'brand', 'get_price']
    search_fields = ['name']
    list_filter = ['name', 'brand', 'category']
    readonly_fields = ['get_price']
