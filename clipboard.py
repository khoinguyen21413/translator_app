# use module pyperclip
import pyperclip
from tkinter import messagebox


class Clipboard:
    def __init__(self, root):
        self.root = root

    def copy_text(self,text):
        if text:
            pyperclip.copy(text)
            print("Clipboard thanh cong: -->>>> ",  pyperclip.paste())
            messagebox.showinfo("Sao chép thành công", "Đã sao chép thành công")
