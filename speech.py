import pyttsx3
import threading

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Toc do doc
        self.engine.setProperty('volume', 1.0)  # Am luong

        voices = self.engine.getProperty('voices')
        # voices[1]: Giong Nu/ voices[0]: Giong nam
        self.engine.setProperty('voice', voices[1].id)

        self.thread = None
        self._stop_flag = threading.Event()
    def speak(self, text, on_done=None):
        if not text:
            return

        # Nếu đang đọc thì dừng lại trước
        self.stop()

        def run():
            print("Text cần đọc:", text)
            self._stop_flag.clear()

            def on_end(name, completed):
                if not self._stop_flag.is_set() and on_done:
                    on_done()

            self.engine.connect('finished-utterance', on_end)
            self.engine.say(text)
            self.engine.runAndWait()

        self.thread = threading.Thread(target=run, daemon=True)
        self.thread.start()

    def stop(self):
        self._stop_flag.set()
        self.engine.stop()
