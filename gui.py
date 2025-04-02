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
        img = Image.open(
            "D:\\O D\\Tin học 6\\python_app\\translator_app\\assets\\transalator_image_1.jpg")
        img = img.resize((180, 114), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        img_label = tk.Label(root, image=img_tk, bg="#FDF6E6")
        img_label.pack()

        # Ngôn ngữ chọn
        frame_lang = tk.Frame(root, bg="gray")
        frame_lang.pack(pady=5)

        lang1 = ttk.Combobox(frame_lang, values=[
            "english", "vietnamese", "french", "spanish"], width=42)
        lang1.set("english")
        lang1.grid(row=0, column=0)

        swap_label = tk.Label(frame_lang, text="↔",
                              font=("Arial", 12), bg="#FDF6E6")
        swap_label.grid(row=0, column=1, padx=10)

        lang2 = ttk.Combobox(frame_lang, values=[
            "english", "vietnamese", "french", "spanish"], width=42)
        lang2.set("vietnamese")
        lang2.grid(row=0, column=2)

        # Ô nhập và hiển thị văn bản
        frame_text = tk.Frame(self.root, bg="#FDF6E6")
        frame_text.pack()

        text_input = tk.Text(frame_text, width=35, height=8)
        text_input.grid(row=0, column=0, padx=10, pady=5)

        text_output = tk.Text(frame_text, width=35, height=8)
        text_output.grid(row=0, column=1, padx=10, pady=5)

        # Frame Buttons
        frame_buttons = tk.Frame(root, bg="#FDF6E6")
        frame_buttons.pack()

        frame_buttons1 = tk.Frame(frame_buttons, bg="#FDF6E6")
        frame_buttons1.pack(side="left")

        frame_buttons2 = tk.Frame(frame_buttons, bg="#FDF6E6")
        frame_buttons2.pack(side="right")

        # Load và chỉnh kích thước copy icon
        img_copy = Image.open(
            "D:\\O D\\Tin học 6\\python_app\\translator_app\\assets\\copy_icon.png")
        img_copy = img_copy.resize((30, 30), Image.LANCZOS)
        photo_copy = ImageTk.PhotoImage(img_copy)

        # Load và chỉnh kích thước sound icon
        img_sound = Image.open(
            "D:\\O D\\Tin học 6\\python_app\\translator_app\\assets\\sound_icon.png")
        img_sound = img_sound.resize((30, 30), Image.LANCZOS)
        photo_sound = ImageTk.PhotoImage(img_sound)

        # Tạo button với ảnh
        sound_btn1 = tk.Button(frame_buttons1, image=photo_sound,
                               command=lambda: print("Đã nghe!"), borderwidth=0)
        sound_btn1.grid(row=0, column=0, padx=10, pady=5)

        # Tạo button với ảnh
        copy_btn1 = tk.Button(frame_buttons1, image=photo_copy,
                              command=lambda: print("Đã copy!"), borderwidth=0)
        copy_btn1.grid(row=0, column=1, padx=10, pady=5)

        # Tạo button với ảnh
        sound_btn2 = tk.Button(frame_buttons2, image=photo_sound,
                               command=lambda: print("Đã nghe!"), borderwidth=0)
        sound_btn2.grid(row=0, column=2, padx=10, pady=5)

        # Tạo button với ảnh
        copy_btn2 = tk.Button(frame_buttons2, image=photo_copy,
                              command=lambda: print("Đã copy!"), borderwidth=0)
        copy_btn2.grid(row=0, column=3, padx=10, pady=5)
