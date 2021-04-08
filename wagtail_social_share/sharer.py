"""
Module containing the methods that
perform the sharing, using the Social Media Strategies.
"""
from django.utils import timezone

from .settings import get_setting


from .models import *


def share_page(page):
    """
    Performs page sharing on the specified social medias.
    """
    # Get the social medias that the page
    # should be shared on
    social_medias = get_setting("SHARE_ON")

    # Append 'Strategy' to the name of each social media
    social_medias = [social_media + "Strategy" for social_media in social_medias]

    # Transform each class string into a actual
    # class ("Foo" --> "<class '__main__.Foo'>")
    strategies = [eval(social_media) for social_media in social_medias]

    # Execute each strategy
    for strategy in strategies:
        # Instantiate strategy, and
        # execute it
        strategy().share(
            post_text=page.share_content,
            post_link=page.share_url,
        )
    # Save that page was shared already
    page.was_shared = True
    # Save share time
    page.shared_at = timezone.now()
    # Save changes
    page.save()
