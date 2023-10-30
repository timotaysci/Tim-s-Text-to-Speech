import requests, uuid, json
import config
# Add your key and endpoint
key = config.transkey
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "westeurope"

path = '/translate'
constructed_url = endpoint + path



params = {
    'api-version': '3.0',
    'from': 'en',
    'to': 'ca-es'
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}



def translate(text):
    body = [{
    'text': text
    }]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response[0]['translations'][0]['text']

print(translate('hello Ona, how are you?!'))
