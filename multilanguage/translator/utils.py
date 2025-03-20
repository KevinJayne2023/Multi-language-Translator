import requests

def translate_with_libre(text, target_lang='en'):
    url = "https://libretranslate.com/translate"
    params = {
        'q': text,
        'source': 'en',  # Assume the source text is in English
        'target': target_lang,
        'format': 'text'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=params, headers=headers)
    if response.status_code == 200:
        return response.json()['translatedText']
    else:
        return "Translation error: " + response.text