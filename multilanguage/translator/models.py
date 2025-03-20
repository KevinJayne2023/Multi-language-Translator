from django.db import models

# Create your models here.
# from modeltranslation.fields import TranslatedField
# from modeltranslation.translator import TranslationOptions

from django.contrib.auth.models import User

# Message model
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient} at {self.timestamp}"

# TranslatedMessage model (optional)
class TranslatedMessage(models.Model):
    original_message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='translations')
    language_code = models.CharField(max_length=10)
    translated_content = models.TextField()

    def __str__(self):
        return f"Translation in {self.language_code} for message {self.original_message.id}"

# Content Model
# class Content(models.Model):
#     content_text = models.TextField()
#     content_text_translated = TranslatedField(models.TextField())

#     def __str__(self):
#         return self.content_text  # Adjust depending on which content you want to display

# class ContentTranslationOptions(TranslationOptions):
#     fields = ('content_text',)  # Fields to be translated using TranslatedField


# # Message Model
# class Message(models.Model):
#     content = models.TextField()
#     content_translated = TranslatedField(models.TextField())
#     sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.content  # Adjust based on which content you want to display

# class MessageTranslationOptions(TranslationOptions):
#     fields = ('content',)  # Fields to be translated using TranslatedField
# class Content(models.Model):
#     content_text = models.TextField()

#     def __str__(self):
#         return self.content_text  # Adjust depending on which content you want to display

# class ContentTranslationOptions(TranslationOptions):
#     fields = ('content_text',)  # Fields to be translated using TranslatedField


# # Message Model
# class Message(models.Model):
#     content = models.TextField()
#     sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.content  # Adjust based on which content you want to display

# class MessageTranslationOptions(TranslationOptions):
#     fields = ('content',)