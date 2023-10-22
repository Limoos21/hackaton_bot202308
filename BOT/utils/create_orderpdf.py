import datetime

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def create_pdf(messages, filename):
    # Загружаем шрифт
    pdfmetrics.registerFont(TTFont('Arial', 'utils/arialmt.ttf'))  # Укажите путь к файлу шрифта

    c = canvas.Canvas(filename)
    c.setFont("Arial", 12)  # Устанавливаем шрифт

    for index, message in enumerate(messages, start=1):
        c.drawString(40, 640, f"Содержание:")
        c.setFont("Arial", 10)  # Устанавливаем шрифт
        c.drawString(20, 620, message[2])
        c.showPage()

    c.save()



