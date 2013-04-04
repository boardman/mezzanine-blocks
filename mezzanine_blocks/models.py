from urlparse import urlparse

from django.db import models
from django.core.cache import cache
from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import settings
from mezzanine.core.models import Slugged, RichText, Orderable
from mezzanine.core.fields import FileField, RichTextField, FileBrowseField
from mezzanine.core.templatetags.mezzanine_tags import thumbnail
from mezzanine.utils.models import AdminThumbMixin
from .category import BlockCategory


class BaseBlock(Slugged):
    """Base Block
    """
    category = models.ForeignKey(BlockCategory, null=True, blank=True)
    login_required = models.BooleanField(_("Login required"), help_text=_("If checked, only logged in users can view this page"), default=False)
    show_title = models.BooleanField(_("Show title"), help_text=_("If checked, show block title"), default=False)

    def save(self, *args, **kwargs):
        super(BaseBlock, self).save(*args, **kwargs)
        cache.delete('%s%s' % ('mezzanine_blocks', self.slug))

    class Meta:
        abstract = True


class Block(BaseBlock):
    """Content Block
    """
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Block')
        verbose_name_plural = _('Blocks')


class RichBlock(BaseBlock, RichText):
    """RichText Block
    """
    class Meta:
        verbose_name = _('Rich Block')
        verbose_name_plural = _('Rich Blocks')


class ImageBlock(BaseBlock, AdminThumbMixin):
    """An image Block
    """
    image = FileBrowseField(verbose_name=_("Image"), format="Image", max_length=255, null=True, blank=True)
    description = RichTextField(_("Description"), blank=True, null=True)
    url = models.URLField(_("External URL"), max_length=255, blank=True, null=True, help_text=_("Optional URL."))

    height = models.IntegerField(_("Height"), default=100, help_text=_("Height in pixels."))
    width = models.IntegerField(_("Width"), default=200, help_text=_("Width in pixels."))
    quality = models.IntegerField(_("Quality"), default=80)

    admin_thumb_field = "image"

    class Meta:
        verbose_name = _('Image Block')
        verbose_name_plural = _('Image Blocks')

    def get_url(self):
        return self.url

    def get_thumb_url(self):
        thumb = None
        if self.admin_thumb_field:
            thumb = getattr(self, self.admin_thumb_field, None)
        if thumb is None:
            return ""

        url = thumbnail(thumb.path, self.carousel_block.width,
            self.carousel_block.height, self.carousel_block.quality)
        # When using differing storage backends,
        # such as Boto and S3 appears that file path
        # can be stored as absolute rather than relative path
        url_obj = urlparse(url)
        if url_obj.scheme not in ['http', 'https']:
            url = "%s%s" % (settings.MEDIA_URL, url)

        return url


class CarouselBlock(BaseBlock):
    """An image carousel block
    """
    content = RichTextField(_("Content"), blank=True)
    interval = models.IntegerField(_("Interval"), default=3,
        help_text="Interval between carousel panels")
    panel_indicators = models.BooleanField("Panel Indicators", default=True,
        help_text="Show direct selection panel indicators in top right of carousel")

    height = models.IntegerField(_("Height"), default=400, help_text=_("Height in pixels."))
    width = models.IntegerField(_("Width"), default=600, help_text=_("Width in pixels."))
    quality = models.IntegerField(_("Image Quality"), default=80)

    def get_interval(self):
        """
        Returns interval in milliseconds as
        expected by javascript
        """
        return self.interval * 1000

    class Meta:
        verbose_name = _("Carousel Block")
        verbose_name_plural = _("Carousel Blocks")


class CarouselPanel(Orderable, AdminThumbMixin):
    carousel_block = models.ForeignKey(CarouselBlock, related_name="panels")
    image = FileBrowseField(_("File"), max_length=200, format="Image")
    url = models.URLField(_("External URL"), max_length=255, blank=True, null=True,
        help_text=_("Optional URL."))
    caption = models.CharField(_("Caption"), max_length=1000, blank=True,
        help_text="Optional caption to display in footer of panel")

    admin_thumb_field = "image"

    class Meta:
        verbose_name = _("Carousel Panel")
        verbose_name_plural = _("Carousel Panels")

    def __unicode__(self):
        return self.caption

    def get_image_url(self):
        thumb = None
        if self.admin_thumb_field:
            thumb = getattr(self, self.admin_thumb_field, None)
        if thumb is None:
            return ""

        url = thumbnail(thumb.path, self.carousel_block.width,
            self.carousel_block.height, self.carousel_block.quality)
        # When using differing storage backends,
        # such as Boto and S3 appears that file path
        # can be stored as absolute rather than relative path
        url_obj = urlparse(url)
        if url_obj.scheme not in ['http', 'https']:
            url = "%s%s" % (settings.MEDIA_URL, url)

        return url
