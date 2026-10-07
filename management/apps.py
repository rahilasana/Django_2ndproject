from django.apps import AppConfig


class ManagementConfig(AppConfig):

    # Default primary key type
    default_auto_field = "django.db.models.BigAutoField"

    # App ka naam
    name = "management"

    # Django app load hone par signals import honge
    def ready(self):
        import management.signals