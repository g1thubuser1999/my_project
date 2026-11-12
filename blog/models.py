from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import UserModel


class BannerModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("title"))
    sub_title = models.CharField(max_length=70, null=True, blank=True, verbose_name=_("sub_title"))
    text = models.CharField(max_length=255, verbose_name=_("text"))
    image = models.ImageField(upload_to='banners/', default='banners/default.png', verbose_name=_("image"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")


class PostModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("title"))
    image = models.ImageField(upload_to='posts/', verbose_name=_("image"))
    sub_title = models.CharField(max_length=255, verbose_name=_("sub_title"))
    text = models.TextField(verbose_name=_("text"))
    quote = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("quote"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class CommentModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_("user")
    )
    post = models.ForeignKey(
        PostModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_("post")
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class CommentLikeModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name=_("user")
    )
    comment = models.ForeignKey(
        CommentModel,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name=_("comment")
    )

    def __str__(self):
        return f"{self.user.username} -> {self.comment.text[:10]}"

    class Meta:
        verbose_name = _("CommentLike")
        verbose_name_plural = _("CommentLikes")


