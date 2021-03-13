"""
Module containing the available Social Media Strategies
to share a Wagtail page.
"""
from abc import ABC, abstractmethod

import twitter
import facebook

from .settings import get_setting


# List of exported objects in 'from ... import *"
__all__ = [
    "FacebookStrategy",
    "TwitterStrategy",
]


class SocialMediaStrategy(ABC):
    """
    Abstract Social Media Strategy.
    Use derivated classes instead.
    """

    @abstractmethod
    def share(self, post_text: str, post_link: str):
        """
        Abstract method that concrete social media
        strategies should implement to share a Wagtail Page.
        """


class FacebookStrategy(SocialMediaStrategy):
    """
    Provides the ability to share a Wagtail Page
    on Facebook.
    """

    def __init__(self):
        """
        Instantiate the Facebook Graph API
        """
        self.api = facebook.GraphAPI(access_token=get_setting("FACEBOOK_ACCESS_TOKEN"))

    def share(self, post_text: str, post_link: str):
        """
        Publishes a post in the feed of the Facebook APP,
        via the Graph API.

        Parameters
        ----------
        post_text: str
            The post text.
        post_link: str
            The page link to share
        """
        # Post to facebook via Graph API
        self.api.put_object(
            parent_object=get_setting("FACEBOOK_APP_ID"),
            connection_name="feed",
            message=post_text,
            link=post_link,
        )


class TwitterStrategy(SocialMediaStrategy):
    """
    Provides the ability to share a Wagtail Page
    on Twitter.
    """

    def __init__(self) -> None:
        """
        Instantiate the Twitter API
        """
        self.api = twitter.Api(
            consumer_key=get_setting("TWITTER_CONSUMER_KEY"),
            consumer_secret=get_setting("TWITTER_CONSUMER_SECRET"),
            access_token_key=get_setting("TWITTER_TOKEN"),
            access_token_secret=get_setting("TWITTER_TOKEN_SECRET"),
        )

    def share(self, post_text: str, post_link: str) -> None:
        """
        Posts a tweet via the Twitter API

        Parameters
        ----------
        post_text: str
            The post text.
        post_link: str
            The page link to share
        """
        # Post tweet via Twitter API
        self.api.PostUpdate(status=f"{post_text}\n{post_link}")
