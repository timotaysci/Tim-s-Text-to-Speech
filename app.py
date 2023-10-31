import os
import uuid
from flask import Flask, render_template, request, redirect, url_for
from azure.storage.blob import BlobServiceClient
import config
app = Flask(__name__)
import ttts_translate as translate
import azure.cognitiveservices.speech as speechsdk
from azure.storage.blob import BlobServiceClient



# Azure Cognitive Services configuration
azure_cognitive_endpoint = config.azureend
azure_cognitive_key = config.key1


# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription= azure_cognitive_key, region='westeurope')
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

speech_config.speech_synthesis_voice_name='ca-ES-EnricNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# blob config
azure_storage_connection_string = config.blobstring


@app.route('/', methods=['GET', 'POST'])
def index():
    user_text = ''
    if request.method == 'POST':
        text = request.form['text']
        user_text = translate.translate(text)

        # Save user_text to Azure Blob Storage
        save_user_text_to_blob(user_text)
        # send to tts
        convert_text_to_speech_and_save(user_text)

    # Retrieve and display the last 10 saved items
    saved_items = get_last_10_saved_items()
    return render_template('index.html', user_text=user_text, saved_items=saved_items)

def save_user_text_to_blob(user_text):
    blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)
    container_name = "user-texts"  # Replace with your desired container name
    container_client = blob_service_client.get_container_client(container_name)
    blob_name = str(uuid.uuid4()) + ".txt"  # Generate a unique blob name

    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(user_text, overwrite=True)

def get_last_10_saved_items():
    blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)
    container_name = "user-texts"  # Replace with your container name
    container_client = blob_service_client.get_container_client(container_name)

    # List blobs and sort them by creation time in descending order
    blobs = sorted(container_client.list_blobs(), key=lambda x: x.creation_time, reverse=True)

    saved_items = []
    for blob in blobs[:10]:  # Retrieve the last 10 blobs
        blob_client = container_client.get_blob_client(blob.name)
        blob_content = blob_client.download_blob()
        saved_text = blob_content.content_as_text()
        saved_items.append(saved_text)

    return saved_items



def convert_text_to_speech_and_save(user_text):
    blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)
    container_name = "user-audio"  # Replace with your desired container name
    container_client = blob_service_client.get_container_client(container_name)
    blob_name = str(uuid.uuid4()) + ".wav"  # Generate a unique blob name with .wav extension

    blob_client = container_client.get_blob_client(blob_name)

    # Generate speech from user_text
    result = speech_synthesizer.speak_text_async(user_text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        # Save the synthesized audio to the Blob Storage
        audio_data = result.audio_data
        content_settings = None  # You can specify other content settings if needed
        blob_client.upload_blob(audio_data, overwrite=True, content_settings=content_settings, content_type="audio/wav")
        print("File saved successfully")
    else:
        print(f"Speech synthesis failed: {result.reason}")






if __name__ == '__main__':
    app.run(debug=True)
