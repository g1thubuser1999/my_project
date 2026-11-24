from modeltranslation.translator import register, TranslationOptions
from .models import AboutModel, BannerModel, Category, PostModel


@register(AboutModel)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(BannerModel)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'text')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'sub_title', 'text')


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'text', 'quote')
