from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "project_apps.myapp"

    def ready(self):
        from myapp import creator

        creator.start()
