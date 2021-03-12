from wagtail_page_sharer.mixins import SocialMediaSharablePageMixin

from django.conf import settings

from wagtail.core.signals import page_published
from wagtail.core.models import get_page_models

from .sharer import share_page
from .settings import get_setting

# Let everyone know when a new page is published
def simple_share_signal(sender, **kwargs):

    # First check if app is in debug mode
    # and if we should perform sharing during
    # debug. Defaults to False
    share_in_debug = get_setting("SHARE_IN_DEBUG", required=False) or False

    if settings.DEBUG and not share_in_debug:
        return
    # Check if the sender is a subclass of 'SocialMediaSharablePageMixin'
    if not issubclass(sender, SocialMediaSharablePageMixin):
        # If the sender does not inherit the mixin, it should not be shared.
        return

    # Check if sender is a registered Wagtail Page
    if not sender in get_page_models():
        return

    # Get page instance
    instance = kwargs["instance"]

    # Check if page was already shared
    if instance.was_shared:
        return

    # Share the page
    share_page(instance)


# Register a receiver
page_published.connect(simple_share_signal)
