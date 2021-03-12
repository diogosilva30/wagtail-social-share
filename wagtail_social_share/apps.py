from django.apps import AppConfig


class WagtailPageSharerConfig(AppConfig):
    name = "wagtail_page_sharer"

    def ready(self):
        import wagtail_page_sharer.signals
