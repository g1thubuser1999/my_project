from modeltranslation.translator import register, TranslationOptions
from products.models import CategoryModel, BrandModel, ColorModel, SizeModel, ProductModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(BrandModel)
class BrandTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ColorModel)
class ColorTranslationOptions(TranslationOptions):
    fields = ('color',)

@register(SizeModel)
class SizeTranslationOptions(TranslationOptions):
    fields = ('size',)

@register(ProductModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'long_description')