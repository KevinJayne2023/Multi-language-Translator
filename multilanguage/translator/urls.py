from django.urls import path
from . import views

urlpatterns = [
    # path('set_language/', set_language, name='set_language'),
    path('chat/', views.chat_view, name='chat_view'), 
]