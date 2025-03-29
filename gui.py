import tkinter as tk
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
