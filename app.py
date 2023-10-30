import os
import uuid
from flask import Flask, render_template, request, redirect, url_for
#from azure.storage.blob import BlobServiceClient
#from azure.cognitiveservices.speech import SpeechConfig, AudioConfig, SpeechSynthesizer
import config
app = Flask(__name__)


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
'''
# The language of the voice that speaks.


# Get text from the console and synthesize to the default speaker.
text = 'Hello, World!' 
speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
'''



'''
# Azure Blob Storage configuration
azure_blob_connection_string = "YOUR_AZURE_BLOB_CONNECTION_STRING"
blob_service_client = BlobServiceClient.from_connection_string(azure_blob_connection_string)
blob_container_name = "your-container-name"
'''

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        if text:
            # Generate a unique filename for the audio file
            filename = f"{str(uuid.uuid4())}.wav"
            
            # Synthesize the text to speech and save it to Azure Blob Storage
            response = speech_synthesizer.speak_text(text)
            #blob_service_client.get_container_client(blob_container_name).upload_blob(name=filename, data=response.get_wav_data())

    # List existing audio files from Azure Blob Storage
    blobs = []
    #container_client = blob_service_client.get_container_client(blob_container_name)
    #for blob in container_client.list_blobs():
     #   blobs.append(blob.name)

    return render_template('index.html', blobs=blobs)

if __name__ == '__main__':
    app.run(debug=True)

