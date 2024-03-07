# BOL-2 Translator App

This Python application allows users to translate text into various languages and convert it into speech. It utilizes the tkinter library for the graphical user interface, Google Translate API for text translation, gTTS (Google Text-to-Speech) for converting text to speech, and playsound for playing audio files. 

## Features
- Translate text from one language to another.
- Choose from a variety of languages for translation.
- Speak the input text.
- Listen to the translated text.
- Delete generated speech files.

## Installation
1. Ensure you have Python installed on your system.
2. Install the required libraries by running: pip install tkinter googletrans gtts playsound.
3. Run the translator_app.py file.

## Usage
1. Enter the desired sentence in the input field.
2. Select the target language from the dropdown menu.
3. Click on the "Translate" button to translate the text.
4. Click on the "Speak Input Text" button to listen to the input text.
5. The translated text will be displayed in the output area.
6. Click on the "Speak Translated Text" button to listen to the translated text.
7. To delete generated speech files, click on the "Delete Speech" button.

## Supported Languages
- French
- Arabic
- Korean
- Hindi
- Urdu
- Chinese
- German
- Italian
- Japanese
- Russian
- Spanish
- Portuguese

## Dependencies
- tkinter: GUI toolkit
- googletrans: Google Translate API
- gtts: Google Text-to-Speech
- playsound: Audio playback

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
