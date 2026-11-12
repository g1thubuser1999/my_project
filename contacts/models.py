from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import UserModel


class ContactModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name=_("user"))
    name = models.CharField(max_length=100, verbose_name=_("name"))
    email = models.EmailField(verbose_name=_("email"))
    subject = models.CharField(max_length=255, verbose_name=_("subject"))
    message = models.TextField(verbose_name=_("message"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return f'{self.name} email on subject {self.subject}'

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')