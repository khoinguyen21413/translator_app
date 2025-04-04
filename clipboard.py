# use module pyperclip
import pyperclip
from tkinter import messagebox
from ttkbootstrap.toast import ToastNotification


def copy_text(text):
    if text:
        pyperclip.copy(text)
        print("Clipboard thanh cong: -->>>> ",  pyperclip.paste())
        # messagebox.showinfo('Thông báo', 'Đã sao chép vào clipboard')
        ToastNotification(
            title="Thông báo", message="Đã sao chép vào clipboard!", duration=3000).show_toast()
