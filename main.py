import pdfplumber
from gtts import gTTS


def get_text():
    file_path = "text.pdf"
    with pdfplumber.PDF(open(file_path, mode='rb')) as pdf_file:
        pages_pdf_text = []
        pdf_text = ""
        [pages_pdf_text.append(pdf_file.pages[page_index].extract_text()) for page_index in range(len(pdf_file.pages))]
        pdf_text = ". ".join(pages_pdf_text)
        return pdf_text.replace('\n', ' ')


def make_audio_file(text, lang):
    audio = gTTS(text=text, lang=lang)
    audio.save("text.mp3")


def main():
    print(get_text())
    make_audio_file(get_text(), 'ru')


if __name__ == '__main__':
    main()
