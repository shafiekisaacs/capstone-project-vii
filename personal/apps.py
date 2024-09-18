from django.apps import AppConfig

class PersonalConfig(AppConfig):
    """Configuration class for the 'personal' app.

    :param AppConfig: The base class for Django application configurations.
    :type AppConfig: class
    :ivar default_auto_field: The default auto field to use for models.
    :vartype default_auto_field: str
    :ivar name: The name of the app.
    :vartype name: str
    """    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal'
