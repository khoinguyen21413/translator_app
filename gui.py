import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class TransalatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng dịch ngôn ngữ - khoi nguyen")
        self.root.geometry("700x406")
        self.root.configure(bg="#FDF6E6")

        # Ảnh minh họa
        img = Image.open("translator_app/assets/transalator_image_1.jpg")
        img = img.resize((180, 114), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        img_label = tk.Label(root, image=img_tk, bg="#FDF6E6")
        img_label.pack()

        # Ngôn ngữ chọn
        frame_lang = tk.Frame(root, bg="gray")
        frame_lang.pack(pady=5)

        lang1 = ttk.Combobox(frame_lang, values=[
            "english", "vietnamese", "french", "spanish"], width=15)
        lang1.set("english")
        lang1.grid(row=0, column=0)

        swap_label = tk.Label(frame_lang, text="↔",
                              font=("Arial", 12), bg="#FDF6E6")
        swap_label.grid(row=0, column=1, padx=10)

        lang2 = ttk.Combobox(frame_lang, values=[
            "english", "vietnamese", "french", "spanish"], width=15)
        lang2.set("vietnamese")
        lang2.grid(row=0, column=2)
