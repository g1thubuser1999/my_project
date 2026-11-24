from django import template

register = template.Library()


@register.simple_tag
def heart_icon(user, product):
    if not user.is_authenticated:
        return 'fa-regular fa-heart'

    if user in product.wishlist.all():
        return 'fa-solid fa-heart'

    return 'fa-regular fa-heart'