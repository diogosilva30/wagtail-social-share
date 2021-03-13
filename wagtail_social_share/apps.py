from django.apps import AppConfig


class WagtailSocialShareConfig(AppConfig):
    name = "wagtail_social_share"

    def ready(self):
        import wagtail_social_share.signals
