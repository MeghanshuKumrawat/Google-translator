from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import speech_recognition as sr
from googletrans import Translator
from tkinter import messagebox
from gtts import gTTS
import playsound
import random
import os


class Google_translator:
    def __init__(self, root):
        self.root = root
        self.root.title('Google Translator')
        self.root.geometry('280x460')
        self.root.config(bg="#4285F4")
        self.google_logo = PhotoImage(file='img\\logo.png')
        self.mic_img = PhotoImage(file="img\\microphone.png")
        self.speaker_img = PhotoImage(file="img\\speaker (1).png")

        self.input_text = ScrolledText(self.root, width=30, height=7)
        self.input_text.place(x=10, y=10)

        self.choose_langauge = ttk.Combobox(self.root, state='readonly',
                                            font=('arial', 10), width=34)

        self.choose_langauge['values'] = (
            'Afrikaans',
            'Albanian',
            'Arabic',
            'Armenian',
            ' Azerbaijani',
            'Basque',
            'Belarusian',
            'Bengali',
            'Bosnian',
            'Bulgarian',
            ' Catalan',
            'Cebuano',
            'Chichewa',
            'Chinese',
            'Corsican',
            'Croatian',
            ' Czech',
            'Danish',
            'Dutch',
            'English',
            'Esperanto',
            'Estonian',
            'Filipino',
            'Finnish',
            'French',
            'Frisian',
            'Galician',
            'Georgian',
            'German',
            'Greek',
            'Gujarati',
            'Haitian Creole',
            'Hausa',
            'Hawaiian',
            'Hebrew',
            'Hindi',
            'Hmong',
            'Hungarian',
            'Icelandic',
            'Igbo',
            'Indonesian',
            'Irish',
            'Italian',
            'Japanese',
            'Javanese',
            'Kannada',
            'Kazakh',
            'Khmer',
            'Kinyarwanda',
            'Korean',
            'Kurdish',
            'Kyrgyz',
            'Lao',
            'Latin',
            'Latvian',
            'Lithuanian',
            'Luxembourgish',
            'Macedonian',
            'Malagasy',
            'Malay',
            'Malayalam',
            'Maltese',
            'Maori',
            'Marathi',
            'Mongolian',
            'Myanmar',
            'Nepali',
            'Norwegian'
            'Odia',
            'Pashto',
            'Persian',
            'Polish',
            'Portuguese',
            'Punjabi',
            'Romanian',
            'Russian',
            'Samoan',
            'Scots Gaelic',
            'Serbian',
            'Sesotho',
            'Shona',
            'Sindhi',
            'Sinhala',
            'Slovak',
            'Slovenian',
            'Somali',
            'Spanish',
            'Sundanese',
            'Swahili',
            'Swedish',
            'Tajik',
            'Tamil',
            'Tatar',
            'Telugu',
            'Thai',
            'Turkish',
            'Turkmen',
            'Ukrainian',
            'Urdu',
            'Uyghur',
            'Uzbek',
            'Vietnamese',
            'Welsh',
            'Xhosa',
            'Yiddish',
            'Yoruba',
            'Zulu',
        )

        self.choose_langauge.place(x=10, y=140)
        self.choose_langauge.current(0)

        self.output_text = ScrolledText(self.root, width=30, height=10)
        self.output_text.place(x=10, y=175)

        button = Button(self.root, text="Translate", cursor="hand2", width=10, command=self.translate)
        button.place(x=190, y=350)

        copy_button = Button(self.root, text="Copy Text", cursor="hand2", width=10, command=self.copy_text)
        copy_button.place(x=100, y=350)

        clear = Button(self.root, text="Clear", cursor="hand2", width=10, command=self.clear)
        clear.place(x=10, y=350)

        Button(self.root, image=self.mic_img, bd=0, bg="white", command=self.listen).place(x=220, y=90)

        Button(self.root, image=self.speaker_img, bd=0, bg="white", command=self.speak).place(x=220, y=303)

        Label(root, image=self.google_logo).place(x=10, y=390)
        Label(root, text="Google", font=('arial black', 30), bg="#4285F4", fg="white").place(x=100, y=385)

    def translate(self):
        language_1 = self.input_text.get(1.0, END)
        cl = self.choose_langauge.get()

        if language_1 == '':
            messagebox.showerror('Google Translator', 'please fill the box')
        else:
            translator = Translator()
            output = translator.translate(language_1, dest=cl)
            self.output_text.delete(1.0, END)
            self.output_text.insert('end', output.text)

    def clear(self):
        self.input_text.delete(1.0, 'end')
        self.output_text.delete(1.0, 'end')

    def copy_text(self):
        self.output_text.clipboard_clear()
        self.output_text.clipboard_append(self.output_text.get(1.0, END))

    def speak(self):
        tts = gTTS(text=self.output_text.get(1.0, END), lang="en")
        r = random.randint(0, 100000)
        audio_file = "audio-"+str(r)+".mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            string = ""
            string = r.recognize_google(audio)
            self.input_text.delete("1.0", END)
            self.input_text.insert(END, string)

root = Tk()
ob = Google_translator(root)
root.mainloop()