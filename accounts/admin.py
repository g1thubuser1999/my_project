from django.db import models
from django.utils.translation import gettext_lazy as _


class BannerModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("title"))
    sub_title = models.CharField(max_length=70, null=True, blank=True, verbose_name=_("sub title"))
    text = models.CharField(max_length=255, verbose_name=_("text"))
    image = models.ImageField(upload_to='banners/', null=True, blank=True, verbose_name=_("image"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")