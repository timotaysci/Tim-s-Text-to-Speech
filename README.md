# Tim's Text to Speech (TTTS)

![logo](g13588.png)

Tim's Text to Speech (TTTS) is a Python web application designed to help users communicate more effectively with individuals who speak Catalan. The application leverages various Azure services, including Azure Cognitive Services for text translation and text-to-speech conversion, and Azure Blob Storage for storing and managing user-generated content. This README provides an overview of the application's functionality, its key components, and how to set it up for your own use.

## Main Features

1. **Translation**: TTTS allows users to enter text in their preferred language, which is then automatically translated into Catalan. This feature is particularly useful when communicating with Catalan-speaking individuals, such as in-laws.

2. **Text-to-Speech Conversion**: The translated text can be converted into speech using Azure Cognitive Services, enabling users to listen to the translated content. This can help in improving pronunciation and understanding.

3. **Audio Storage**: The application saves both the translated text and the corresponding speech audio to Azure Blob Storage for easy access and sharing. Users can retrieve the audio files later, making it convenient for ongoing communication.

4. **History**: TTTS keeps a history of the last 10 translated and synthesized items, providing a quick way to revisit and reuse previous translations.

## Application Components

The TTTS application comprises several key components:

- **Flask Web Application**: TTTS is built using the Flask web framework, making it accessible through a web browser. Users can input text, initiate translations, and listen to speech output.

- **Azure Cognitive Services**: The application uses Azure Cognitive Services, specifically the Text Translator and Text-to-Speech services, to handle translation and speech synthesis. These services are configured to work seamlessly with the application.

- **Azure Blob Storage**: Azure Blob Storage is used to store both the translated text and the synthesized audio files. This allows users to access and share content easily.

## Getting Started

To set up TTTS for your use, follow these steps:

1. **Azure Configuration**: Ensure that you have an Azure account and the required services (Cognitive Services and Blob Storage) configured. Update the `config.py` file with your Azure Cognitive Services endpoint, key, and Blob Storage connection string.

2. **Python Environment**: 

``pip install virtualenv``

``cd /path/to/project``

``virtualenv TTTS``

``source TTTS/bin/activate``

``pip install -r requirements.txt``




3. **Running the Application**: Execute the script to start the Flask application by running `python app.py`. The application should be accessible in your web browser at `http://localhost:5000`.

4. **Usage**: Enter the text you want to translate in the input field, and click "Translate." The translated text will be displayed, and you can listen to the speech output. Both the text and audio are stored in Azure Blob Storage.

## Contributing

Feel free to contribute to the development of TTTS by submitting pull requests or reporting issues. You can find the source code on GitHub.

## License

This project is licensed under the MIT License, allowing you to use and modify the code for your needs.

## Support

If you encounter any issues or have questions about using TTTS, please open an issue on GitHub.

Tim's Text to Speech is a practical solution for bridging language barriers and improving communication with Catalan-speaking individuals. Give it a try, and make conversations with your in-laws and other Catalan speakers more enjoyable.
