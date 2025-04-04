import pyttsx3


# def speak_text(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Toc do doc
        self.engine.setProperty('volume', 1.0)  # Am luong

        voices = self.engine.getProperty('voices')
        # voices[1]: Giong Nu/ voices[0]: Giong nam
        self.engine.setProperty('voice', voices[1].id)

    def speak(self, text):
        if text:
            print("Text can doc: ", text)
            self.engine.say(text)
            self.engine.runAndWait()
