from django.apps import AppConfig


class DeploydocusConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "deploydocus"

    def ready(self):
        import deploydocus.signals  # noqa
