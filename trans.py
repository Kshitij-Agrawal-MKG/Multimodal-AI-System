import requests
import uuid
import json

# Replace with your actual API key and region
key = "4XDf6c8CVYvKLj9XqzMFMknPrHYKiVFprMz80QQwA3i9rj0NgeFlJQQJ99BBACGhslBXJ3w3AAAbACOGKxip"
location = "centralindia"
endpoint = "https://api.cognitive.microsofttranslator.com"
def translate_text(text, target_language):
    

    # Dictionary mapping language names to their corresponding codes
    language_map = {
        "English": "en",
        "Tamil": "ta",
        "Hindi": "hi",
        "Telugu": "te",
        "Marathi": "mr",
        "Bengali": "bn"  # Corrected language name here
    }
    
    # Convert the language to lowercase and check if it's valid
    language_code = language_map.get(target_language, None)
    
    # If the language is not recognized, return an error message
    if language_code is None:
        return "Invalid language"
    
    # Return the corresponding language code
    # return language_code

    # API path and URL construction
    path = '/translate'
    constructed_url = endpoint + path

    # Set up parameters for the request
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': language_code
    }

    # Set up headers for the request
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Body of the request containing the text to be translated
    body = [{'text': text}]

    # Send the POST request
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    
    # Check if the request was successful
    if request.status_code != 200:
        print(f"Error: {request.status_code}")
        print(request.text)
        return None

    # Parse the response JSON
    response = request.json()

    # Extract and return the translated text (for single language)
    translated_text = response[0]['translations'][0]['text']
    
    return translated_text
