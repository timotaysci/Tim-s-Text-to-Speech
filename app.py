import os
import uuid
from flask import Flask, render_template, request, redirect, url_for
#from azure.storage.blob import BlobServiceClient
#from azure.cognitiveservices.speech import SpeechConfig, AudioConfig, SpeechSynthesizer
import config
app = Flask(__name__)
import ttts_translate as translate

# Azure Cognitive Services configuration
azure_cognitive_endpoint = config.azureend
azure_cognitive_key = config.key1

print(azure_cognitive_endpoint)

import os
import azure.cognitiveservices.speech as speechsdk

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription= azure_cognitive_key, region='westeurope')
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

speech_config.speech_synthesis_voice_name='ca-ES-EnricNeural'






speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)





@app.route('/', methods=['GET', 'POST'])
def index():
    user_text = ''
    if request.method == 'POST':
        text = request.form['text']
        user_text = translate.translate(text)
    return render_template('index.html', user_text=user_text )

if __name__ == '__main__':
    app.run(debug=True)

