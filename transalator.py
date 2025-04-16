from mtranslate import translate

class GoogleTrans:
    def __init__(self, src_lang='auto', dest_lang='en'):
        """
        Khởi tạo class với ngôn ngữ nguồn và đích.
        :param src_lang: Ngôn ngữ nguồn (mặc định 'auto')
        :param dest_lang: Ngôn ngữ đích (mặc định 'en' - English)
        """
        self.src_lang = src_lang
        self.dest_lang = dest_lang

    def translate_text(self, text):
        """
        Dịch văn bản sang ngôn ngữ đích.
        :param text: Văn bản cần dịch
        :return: Văn bản đã dịch
        """        
        try:
            return translate(text, self.dest_lang, self.src_lang)
        except Exception as e:
            return f"Lỗi dịch: {e}"