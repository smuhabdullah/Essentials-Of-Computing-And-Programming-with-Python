import tkinter as tk
from tkinter import ttk
from googletrans import Translator
import gtts
import playsound
import os
import uuid

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("BOL_2")

        # Set background color to sky green
        master.configure(background="#87CEEB")

        # Set up the heading label
        self.heading_label = ttk.Label(master, text="BOL-2 (Text to Speech and Language Translator)", font=("Helvetica", 16, "bold"), background="#87CEEB")
        self.heading_label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        # Set up the label for entering a sentence
        self.label = ttk.Label(master, text="Enter a sentence:", font=("Helvetica", 12))
        self.label.grid(row=1, column=0, columnspan=2, pady=10, padx=5, sticky="w")

        # Entry widget for user input
        self.entry = ttk.Entry(master, font=("Helvetica", 13), width=50)
        self.entry.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

        # Label for selecting language
        self.language_label = ttk.Label(master, text="Select a language:", font=("Helvetica", 12))
        self.language_label.grid(row=3, column=0, sticky="w", pady=5, padx=5)

        # Combobox for selecting language
        self.language_var = tk.StringVar()
        self.language_combobox = ttk.Combobox(master, textvariable=self.language_var, state="readonly", width=20)
        self.language_combobox['values'] = ["French", "Arabic", "Korean", "Hindi", "Urdu", "Chinese", "German", "Italian", "Japanese", "Russian", "Spanish", "Portuguese"]
        self.language_combobox.current(0)
        self.language_combobox.grid(row=3, column=1, pady=5, padx=5)

        # Button for translating text
        self.translate_button = ttk.Button(master, text="Translate", command=self.translate_text, style="Custom.TButton")
        self.translate_button.grid(row=4, column=0, pady=5, padx=5)

        # Button for speaking input text
        self.speak_button_input = ttk.Button(master, text="Speak Input Text", command=self.speak_input_text, style="Custom.TButton")
        self.speak_button_input.grid(row=4, column=1, pady=5, padx=5)

        # Button for exiting the application
        self.exit_button = ttk.Button(master, text="Exit", command=self.master.quit, style="Custom.TButton")
        self.exit_button.grid(row=4, column=3, pady=5, padx=5)

        # Text widget for displaying output
        self.output_text = tk.Text(master, wrap=tk.WORD, font=("Helvetica", 13), height=10, width=100)
        self.output_text.grid(row=5, column=0, columnspan=4, pady=5, padx=5, rowspan=2)

        # Button for speaking translated text
        self.speak_button_translated = ttk.Button(master, text="Speak Translated Text", command=self.speak_translated_text, style="Custom.TButton")
        self.speak_button_translated.grid(row=7, column=0, columnspan=4, pady=5, padx=5)

        # Button for deleting speech files
        self.delete_button = ttk.Button(master, text="Delete Speech", command=self.delete_mp3_files, style="Custom.TButton")
        self.delete_button.grid(row=8, column=0, columnspan=4, pady=5, padx=5)
        
        # List to store audio file paths
        self.audio_files = []

        # Custom style for the buttons to add padding
        s = ttk.Style()
        s.configure("Custom.TButton", padding=(10, 10))

    # Translate text entered by the user
    def translate_text(self):
        text = self.entry.get()
        dest_lang = self.get_dest_lang()
        translator = Translator()
        translated_text = translator.translate(text, dest=dest_lang).text
        self.output_text.insert(tk.END, f"{translated_text}\n")

    # Speak the input text entered by the user
    def speak_input_text(self):
        text = self.entry.get()
        lang = self.get_dest_lang()
        tts = gtts.gTTS(text, lang=lang)
        filename = f"input_{uuid.uuid4().hex}.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        self.audio_files.append(filename)

    # Speak the translated text
    def speak_translated_text(self):
        translated_text = self.output_text.get("end - 2 lines linestart", "end")
        lang = self.get_dest_lang()
        tts = gtts.gTTS(translated_text, lang=lang)
        filename = f"translated_{uuid.uuid4().hex}.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        self.audio_files.append(filename)

    # Delete speech files
    def delete_mp3_files(self):
        for filename in self.audio_files:
            if os.path.exists(filename):
                os.remove(filename)
                self.output_text.insert(tk.END, f"{filename} deleted\n")
        self.audio_files.clear()

    # Get the language code corresponding to the selected language
    def get_dest_lang(self):
        languages = {
            "French": "fr",
            "Arabic": "ar",
            "Korean": "ko",
            "Hindi": "hi",
            "Urdu": "ur",
            "Chinese": "zh-CN",
            "German": "de",
            "Italian": "it",
            "Japanese": "ja",
            "Russian": "ru",
            "Spanish": "es",
            "Portuguese": "pt"
        }
        return languages.get(self.language_combobox.get())

def main():
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()





