import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from clipboard import Clipboard
from speech import TextToSpeech
from transalator import GoogleTrans
from tkinter import messagebox


class TransalatorApp:
    LANGUAGE_CODES = {
        "auto": "auto",
        "english": "en",
        "vietnamese": "vi",
        "french": "fr",
        "korean": "ko",
        "japanese": "ja"
    }

    background_color = '#FDF6E6'

    def __init__(self, root):
        self.root = root
        self.root.title("Translator App by Khoi Nguyen")
        self.root.geometry("650x420")
        self.root.configure(bg=self.background_color)
        # Khóa không cho resize theo chiều ngang và dọc
        self.root.resizable(False, False)
        self.create_menu()

        # Style cho ttk widgets
        self.style = ttk.Style()
        self.style.theme_use("default")

        default_font = ("Arial", 10)

        self.style.configure("TFrame", background=self.background_color)
        self.style.configure("TLabel", background=self.background_color, font=default_font)
        self.style.configure("TCombobox", font=default_font, padding=3)
        self.style.configure("TButton", background="#D0E1F9", foreground="black",
                             font=("Arial", 10, "bold"), padding=5)
        self.style.map("TButton", background=[("active", "#AECBEA")])

        # Custom style for Translate button
        self.style.configure("My.TButton", background="#D0E1F9", font=("Arial", 11, "bold"))

        # Ảnh minh họa
        img = Image.open(
            "D:\\O D\\Tin học 6\\python_app\\translator_app\\assets\\transalator_image_1.jpg").resize((180, 114), Image.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img)
        img_label = tk.Label(root, image=self.img_tk, bg=self.background_color)
        img_label.pack()

        language_list = list(self.LANGUAGE_CODES.keys())
        language_list_no_first = language_list[1:]

        # Ngôn ngữ chọn
        frame_lang = ttk.Frame(root)
        frame_lang.pack(pady=5)

        self.lang1_var = tk.StringVar(value="english")
        self.lang2_var = tk.StringVar(value="vietnamese")

        lang1 = ttk.Combobox(frame_lang, textvariable=self.lang1_var,
                             values=language_list, width=37, state="readonly")
        lang1.grid(row=0, column=0)

        swap_btn = ttk.Button(frame_lang, text="↔", width=3,
                      command=self.swap_languages)
        swap_btn.grid(row=0, column=1, padx=12)

        lang2 = ttk.Combobox(frame_lang, textvariable=self.lang2_var,
                             values=language_list_no_first, width=37, state="readonly")
        lang2.grid(row=0, column=2)

        # Khung nhập và hiển thị văn bản
        frame_text = ttk.Frame(self.root)
        frame_text.pack()

        self.text_input = tk.Text(frame_text, width=31, height=8)
        self.text_input.grid(row=0, column=0, padx=22, pady=5)

        self.text_output = tk.Text(frame_text, width=31, height=8)
        self.text_output.grid(row=0, column=1, padx=22, pady=5)

        # Căn các button về hai bên
        frame_buttons = ttk.Frame(self.root)
        frame_buttons.pack(fill="x", pady=5, padx=40)

        frame_buttons1 = ttk.Frame(frame_buttons)
        frame_buttons1.pack(side="left")

        frame_buttons2 = ttk.Frame(frame_buttons)
        frame_buttons2.pack(side="right")


        # Icon
        img_copy = Image.open(
            "D:\\O D\\Tin học 6\\python_app\\translator_app\\assets\\copy_icon.png").resize((30, 30), Image.LANCZOS)
        self.photo_copy = ImageTk.PhotoImage(img_copy)

        img_sound = Image.open(
            "D:\\O D\\Tin học 6\\python_app\\translator_app\\assets\\sound_icon.png").resize((30, 30), Image.LANCZOS)
        self.photo_sound = ImageTk.PhotoImage(img_sound)

        # Các nút âm thanh & sao chép
        sound_btn1 = ttk.Button(frame_buttons1, image=self.photo_sound,
                                command=lambda: self.speak_text(self.text_input.get("1.0", "end").strip()))
        sound_btn1.grid(row=0, column=0, padx=10, pady=5)

        copy_btn1 = ttk.Button(frame_buttons1, image=self.photo_copy,
                               command=lambda: self.copy_text(self.text_input.get("1.0", "end").strip()))
        copy_btn1.grid(row=0, column=1, padx=10, pady=5)

        sound_btn2 = ttk.Button(frame_buttons2, image=self.photo_sound,
                                command=lambda: self.speak_text(self.text_output.get("1.0", "end").strip()))
        sound_btn2.grid(row=0, column=0, padx=10, pady=5)

        copy_btn2 = ttk.Button(frame_buttons2, image=self.photo_copy,
                               command=lambda: self.copy_text(self.text_output.get("1.0", "end").strip()))
        copy_btn2.grid(row=0, column=1, padx=10, pady=5)

        # Nút Translate
        transalate_btn = ttk.Button(self.root, text="Translate", style="My.TButton",
                            command=lambda: self.translate_text(self.lang1_var, self.lang2_var, self.text_input, self.text_output))
        transalate_btn.pack(pady=10, ipadx=100)  # Tăng width đáng kể

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        feature_menu = tk.Menu(menu_bar, tearoff= 0)
        feature_menu.add_command(label="Copy", command=lambda: self.copy_text(self.text_output.get("1.0", "end").strip()))
        feature_menu.add_command(label="Speak", command=lambda: self.speak_text(self.text_output.get("1.0", "end").strip()))
        feature_menu.add_command(label="Translate", command=lambda: self.translate_text(self.lang1_var, self.lang2_var, self.text_input, self.text_output))
        menu_bar.add_cascade(label="Feature", menu=feature_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Instruct", command=self.show_help)
        help_menu.add_command(label="Introduce", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        self.root.config(menu=menu_bar)

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

    def show_help(self):
        messagebox.showinfo("Instruct", "Application that helps translate languages. You can copy, listen and translate with this app.")

    def show_about(self):
        messagebox.showinfo("Introduce", "Translator\nVersion 1.1\nAuthor: Khoi Nguyen")

    def speak_text(self, text):
        tts = TextToSpeech()
        tts.speak(text=text)

    def copy_text(self, text):
        cl = Clipboard(self.root)
        cl.copy_text(text)

    def swap_languages(self):
        lang1 = self.lang1_var.get()
        lang2 = self.lang2_var.get()
        self.lang1_var.set(lang2)
        self.lang2_var.set(lang1)

