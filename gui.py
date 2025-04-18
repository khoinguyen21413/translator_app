import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from clipboard import Clipboard
from speech import TextToSpeech
from transalator import GoogleTrans


class TransalatorApp:
    LANGUAGE_CODES = {
            "auto": "auto",
            "english": "en",
            "vietnamese": "vi",
            "french": "fr",
            "korean": "ko",
            "japanese": "ja"
    }

    background_color ='#FDF6E6'

    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng dịch ngôn ngữ - khoi nguyen")
        self.root.geometry("600x406")
        self.root.configure(bg=self.background_color)

        # Ảnh minh họa
        img = Image.open(
            "D:\\O D\\Tin học 6\\python_app\\translator_app\\assets\\transalator_image_1.jpg").resize((180, 114), Image.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img)
        img_label = tk.Label(root, image=self.img_tk, bg=self.background_color)
        img_label.pack()

        language_list = list(self.LANGUAGE_CODES.keys())
        language_list_no_first = language_list[1:]

        # Ngôn ngữ chọn
        frame_lang = tk.Frame(root, bg="gray")
        frame_lang.pack(pady=5)

        # Biến StringVar để liên kết với OptionMenu
        self.lang1_var = tk.StringVar()
        self.lang1_var.set("english")  # mặc định

        self.lang2_var = tk.StringVar()
        self.lang2_var.set("vietnamese")  # mặc định

        # OptionMenu thay cho Combobox
        lang1 = tk.OptionMenu(frame_lang, self.lang1_var, *language_list)
        lang1.config(width=32)  # giống Combobox
        lang1.grid(row=0, column=0)

        swap_label = tk.Label(frame_lang, text="↔",
                            font=("Arial", 12), bg=self.background_color)
        swap_label.grid(row=0, column=1, padx=10)

        lang2 = tk.OptionMenu(frame_lang, self.lang2_var, *language_list_no_first)
        lang2.config(width=32)
        lang2.grid(row=0, column=2)

        # Ô nhập và hiển thị văn bản
        frame_text = tk.Frame(self.root, bg=self.background_color)
        frame_text.pack()

        text_input = tk.Text(frame_text, width=35, height=8)
        text_input.grid(row=0, column=0, padx=15, pady=5)

        text_output = tk.Text(frame_text, width=35, height=8)
        text_output.grid(row=0, column=1, padx=15, pady=5)

        # Frame Buttons
        frame_buttons = tk.Frame(root, bg=self.background_color)
        frame_buttons.pack()

        frame_buttons1 = tk.Frame(frame_buttons, bg=self.background_color)
        frame_buttons1.pack(side="left")

        frame_buttons2 = tk.Frame(frame_buttons, bg=self.background_color)
        frame_buttons2.pack(side="right")

        # Load và chỉnh kích thước copy icon
        img_copy = Image.open(
            "D:\\O D\\Tin học 6\\python_app\\translator_app\\assets\\copy_icon.png")
        img_copy = img_copy.resize((30, 30), Image.LANCZOS)
        self.photo_copy = ImageTk.PhotoImage(img_copy)

        # Load và chỉnh kích thước sound icon
        img_sound = Image.open(
            "D:\\O D\\Tin học 6\\python_app\\translator_app\\assets\\sound_icon.png")
        img_sound = img_sound.resize((30, 30), Image.LANCZOS)
        self.photo_sound = ImageTk.PhotoImage(img_sound)

        # Tạo button với ảnh
        sound_btn1 = tk.Button(frame_buttons1, image=self.photo_sound,
                               command=lambda: self.speak_text(text_input.get("1.0", "end").strip()), borderwidth=0)
        sound_btn1.grid(row=0, column=0, padx=10, pady=5)

        # Tạo button với ảnh
        copy_btn1 = tk.Button(frame_buttons1, image=self.photo_copy,
                              command=lambda: self.copy_text(text_input.get("1.0", "end").strip()), borderwidth=0)
        copy_btn1.grid(row=0, column=1, padx=10, pady=5)

        # Tạo button với ảnh
        sound_btn2 = tk.Button(frame_buttons2, image=self.photo_sound,
                               command=lambda: self.speak_text(text_output.get("1.0", "end").strip()), borderwidth=0)
        sound_btn2.grid(row=0, column=0, padx=10, pady=5)

        # Tạo button với ảnh
        copy_btn2 = tk.Button(frame_buttons2, image=self.photo_copy,
                              command=lambda: self.copy_text(text_output.get("1.0", "end").strip()), borderwidth=0)
        copy_btn2.grid(row=0, column=1, padx=10, pady=5)

        # Tạo button chức năng dịch
        transalate_btn = tk.Button(self.root, text="Translate", font=("Arial", 12, "bold"), bg="#D0E1F9",
                                   relief="raised", command=lambda: self.translate_text(self.lang1_var, self.lang2_var, text_input, text_output), width=35)
        transalate_btn.pack(pady=10)

    def translate_text(self, lang1, lang2, text_input, text_output):
        text = text_input.get("1.0", "end").strip()
        src_lang = lang1.get()
        dest_lang = lang2.get()

        if not text:
            text_output.delete("1.0", "end")
            text_output.insert("1.0", "Vui lòng nhập văn bản cần dịch.")
            return

        src_lang_code = self.LANGUAGE_CODES[src_lang]
        dest_lang_code = self.LANGUAGE_CODES[dest_lang]
        translator = GoogleTrans(src_lang_code, dest_lang_code)
        result = translator.translate_text(text)

        text_output.delete("1.0", "end")
        text_output.insert("1.0", result)

    def speak_text(self, text):
        tts = TextToSpeech()
        tts.speak(text=text)

    def copy_text(self, text):
        cl = Clipboard()
        cl.copy_text(text)
