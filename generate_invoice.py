import random
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors

def generate_random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime.now()
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

def generate_invoice():
    fatura_no = random.randint(100000, 999999)
    tarih = generate_random_date().strftime("%d.%m.%Y")
    filename = f"fatura_{fatura_no}.pdf"

    ürünler = [
        ("Web Hosting", random.randint(1, 3), random.randint(100, 500)),
        ("Alan Adı Kaydı", 1, random.randint(50, 200)),
        ("SSL Sertifikası", 1, random.randint(100, 300)),
        ("Sunucu Bakımı", random.randint(1, 2), random.randint(200, 600))
    ]

    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 20)
    c.drawString(30 * mm, height - 30 * mm, "FATURA")

    c.setFont("Helvetica", 12)
    c.drawRightString(width - 30 * mm, height - 30 * mm, f"Fatura No: {fatura_no}")
    c.drawRightString(width - 30 * mm, height - 40 * mm, f"Tarih: {tarih}")

    c.drawString(30 * mm, height - 50 * mm, "Satıcı:")
    c.drawString(35 * mm, height - 58 * mm, "NeoTech Bilişim Hizmetleri A.Ş.")
    c.drawString(35 * mm, height - 66 * mm, "İstiklal Mah. Teknokent Sok. No:42/1 Kadıköy/İstanbul")
    c.drawString(35 * mm, height - 74 * mm, "Vergi No: 1234567890")

    c.drawString(30 * mm, height - 90 * mm, "Alıcı:")
    c.drawString(35 * mm, height - 98 * mm, "Deneme Kullanıcısı")
    c.drawString(35 * mm, height - 106 * mm, "Deneme Mah. Örnek Cad. No:99/5 Beşiktaş/İstanbul")
    c.drawString(35 * mm, height - 114 * mm, "Vergi No: 9876543210")

    c.setFont("Helvetica-Bold", 12)
    y = height - 130 * mm
    c.drawString(30 * mm, y, "Ürün/Hizmet")
    c.drawString(100 * mm, y, "Adet")
    c.drawString(120 * mm, y, "Birim Fiyat (₺)")
    c.drawString(160 * mm, y, "Tutar (₺)")
    c.setFont("Helvetica", 12)
    y -= 10 * mm

    ara_toplam = 0
    for ad, adet, fiyat in ürünler:
        toplam = adet * fiyat
        c.drawString(30 * mm, y, ad)
        c.drawString(100 * mm, y, str(adet))
        c.drawString(120 * mm, y, f"{fiyat:.2f}")
        c.drawString(160 * mm, y, f"{toplam:.2f}")
        y -= 8 * mm
        ara_toplam += toplam

    kdv = ara_toplam * 0.20
    genel_toplam = ara_toplam + kdv

    y -= 10 * mm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30 * mm, y, f"Ara Toplam: {ara_toplam:.2f} ₺")
    y -= 8 * mm
    c.drawString(30 * mm, y, f"KDV (%20): {kdv:.2f} ₺")
    y -= 8 * mm
    c.drawString(30 * mm, y, f"Genel Toplam: {genel_toplam:.2f} ₺")

    y -= 20 * mm
    c.setFont("Helvetica", 12)
    c.drawString(30 * mm, y, "Ödeme Şekli: Kredi Kartı")
    c.drawString(30 * mm, y - 8 * mm, "Fatura Durumu: ÖDENDİ")

    c.setFont("Helvetica-Bold", 50)
    c.setFillColor(colors.red)
    c.rotate(25)
    c.drawCentredString(width / 2, height / 2, "GEÇERSİZDİR")
    c.setFillColor(colors.black)
    c.rotate(-25)

    c.save()
    print(f"{filename} oluşturuldu.")

if __name__ == "__main__":
    generate_invoice()
