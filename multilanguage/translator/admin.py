from django.contrib import admin
from .models import Message, TranslatedMessage

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp')  # Customize to your needs
    list_filter = ('timestamp', 'sender', 'recipient')
    search_fields = ('content',)

class TranslatedMessageAdmin(admin.ModelAdmin):
    list_display = ('original_message', 'language_code', 'translated_content')
    list_filter = ('language_code',)
    search_fields = ('translated_content',)
    raw_id_fields = ('original_message',)  # This makes it easier to select associated messages

# Register the admin classes with the associated models
admin.site.register(Message, MessageAdmin)
admin.site.register(TranslatedMessage, TranslatedMessageAdmin)