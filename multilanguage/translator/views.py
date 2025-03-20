from django.shortcuts import render, redirect
from django.utils.translation import activate
from .utils import translate_with_libre

def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        target_lang = request.POST.get('language', 'en')  # Default to English
        try:
            translated_message = translate_with_libre(message, target_lang)
            return render(request, 'index.html', {'translated_message': translated_message})
        except Exception as e:
            return render(request, 'index.html', {'error': "Failed to translate message: " + str(e)})
    return render(request, 'index.html')

def set_language(request):
    language_code = request.GET.get('language', 'en')
    activate(language_code)
    response = redirect('home')  # Replace 'home' with your home view's name
    response.set_cookie('django_language', language_code)
    return response