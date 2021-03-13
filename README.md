# WAGTAIL-SOCIAL-SHARE

Auto-share Wagtail Pages on Social Medias.

# Installation :package:

From PyPi repository:

```
pip install wagtail-social-share
```

From source code:

```
git clone https://github.com/spamz23/wagtail-social-share.git
virtualenv venv
pip install -r requirements.txt
```

# How to use it?

This package is designed to be easily integrable and flexible! :fire:
Here's how you can get started in a few simple steps:

1. Add `wagtail_social_share` to your `INSTALLED_APPS` inside Django settings:

```python
INSTALLED_APPS = (
    # ...
    'wagtail_social_share',
)
```

2. Marking a page as sharable:

```python

from wagtail.core.models import Page

from wagtail_social_share.mixins import SocialMediaSharablePageMixin

class BlogPostPage(SocialMediaSharablePageMixin, Page):
    """
    Your custom Wagtail Page model.
    Just inherit the `SocialMediaSharablePageMixin` to
    make it automatically sharable.
    """
```

3. Add some configuration settings (inside your Django configs):

```python
# ...

WAGTAIL_SOCIAL_SHARE={
    # The social medias that the pages should be shared on
    "SHARE_ON":["Facebook", "Twitter"]

    # In case you use 'Facebook', you need the following two settings:
    "FACEBOOK_ACCESS_TOKEN": "xxxxxxxxxx", # Replace it with your facebook access token
    "FACEBOOK_APP_ID": "xxxxxxxxxx", # Replace it with your facebook app id

    # In case you use 'Twitter', you need the following four settings:
    "TWITTER_CONSUMER_KEY" : "xxxxxxxxxx", # Replace it with your Twitter Consumer Key
    "TWITTER_CONSUMER_SECRET" : "xxxxxxxxxx", # Replace it with your Twitter Consumer secret
    "TWITTER_TOKEN" : "xxxxxxxxxx", # Replace it with your Twitter Token
    "TWITTER_TOKEN_SECRET" : "xxxxxxxxxx", # Replace it with your Twitter Token Secret

    # Additional Options (Optional):
    "SHARE_IN_DEBUG" : False, # Whether to perform page sharing in DEBUG Mode (defaults to False)
}
```

That's all the basic configuration needed!

Extra details:

## Customizing the share URL

`wagtail_social_share` provides you the ability to customize the URL that will be shared.
This is useful for example if you are using a **headless Wagtail**, therefore you don't know
in advance what the URL will look like in the frontend.
How to do this? Easy:

```python

from wagtail.core.models import Page

from wagtail_social_share.mixins import SocialMediaSharablePageMixin

class BlogPostPage(SocialMediaSharablePageMixin, Page):
    """
    `SocialMediaSharablePageMixin` uses a property called `share_url`,
    that will by default, return the property `full_url` of a Wagtail Page.
    To provide a custom URL for a page, you can simply override this property.
    """

    @property
    def share_url(self):
        """
        Provide your custom logic for the URL.
        In this example we assume the URLs for the Blog Posts will be:
        'https://myawesomeblog.com/posts/{blog-post-slug}'
        """
        # Build the URL with the slug
        return "https://myawesomeblog.com/posts/" + self.slug
```

## Exposing the share URL to the Wagtail API

`wagtail_social_share` provides you the ability to easily expose the `share_url` property,
to the Wagtail API.
In case you are not familiar with the Wagtail API, please refeer to their [documentation](https://docs.wagtail.io/en/v2.12.3/advanced_topics/api/index.html).

```python

from wagtail.core.models import Page

from wagtail_social_share.mixins import SocialMediaSharablePageMixin

class BlogPostPage(SocialMediaSharablePageMixin, Page):
    """
    `SocialMediaSharablePageMixin` already provides its own
    `api_fields`. Thefore, you can just simply add them to yours.
    """

    # ... define your page fields

    api_fields = [
        # ... Define your own API Fields
    ] + SocialMediaSharablePageMixin.api_fields
```