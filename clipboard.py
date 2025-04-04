# use module pyperclip
import pyperclip
from ttkbootstrap.toast import ToastNotification


class Clipboard:
    def __init__(self):
        pass

    def copy_text(text):
        if text:
            pyperclip.copy(text)
            print("Clipboard thanh cong: -->>>> ",  pyperclip.paste())
            ToastNotification(
                title="Thông báo", message="Đã sao chép vào clipboard!", duration=3000).show_toast()
