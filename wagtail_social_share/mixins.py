"""
Contains the Mixins that Wagtail Page models can inherit.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.api import APIField


from .edit_handlers import ReadOnlyPanel


class SocialMediaSharablePageMixin(models.Model):
    """
    Mixin that Wagtail Page models must inherit to
    become sharable on social medias.
    """

    # Indicates if page was already shared
    was_shared = models.BooleanField(verbose_name=_("Partilhado"), default=False)
    # The time it was shared
    shared_at = models.DateTimeField(
        verbose_name=_("Partilhado a"), blank=True, null=True
    )

    @property
    def share_content(self):
        """
        The content that will be shared on a social media.

        Defaults to:
            `self.search_description`

        Can be overriden to customize what gets shared.
        """
        return self.search_description

    @property
    def share_url(self):
        """
        The URL that will be shared. Defaults to Wagtail's Page
        'full_url' property.

        Can be overriden to provide custom
        behavior on building the URL. This is usefull when using
        headless Wagtail, where the backend does not know in advance
        the URL that the page will have in the frontend.
        """
        return self.url

    content_panels = [
        ReadOnlyPanel("was_shared", heading=_("Partilhado")),
        ReadOnlyPanel("shared_at", heading=_("Partilhado a")),
    ]

    # Expose to Wagtail API
    api_fields = [
        APIField("share_url"),
    ]

    class Meta:  # noqa
        abstract = True
