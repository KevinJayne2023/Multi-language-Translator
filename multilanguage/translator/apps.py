from django.apps import AppConfig
from modeltranslation.translator import translator, TranslationOptions
from .models import Message

class MessageTranslationOptions(TranslationOptions):
    fields = ('content',) 

class TranslatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'translator'  

    def ready(self):
        translator.register(Message, MessageTranslationOptions)