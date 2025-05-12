# SAHTEKAR

🧾 Otomatik Sahte Fatura Üretici (PDF)

**Sahtekar**, sahte ve geçersiz fatura örnekleri oluşturmak için geliştirilen bir Python programıdır. Rastgele tarih, fatura numarası, ürün isimleri ve fiyatlar ile PDF çıktısı üretir. Tamamen **eğitim ve test** amaçlarla kullanılması için tasarlanmıştır.

> ⚠️ Üretilen faturalar **geçersizdir** ve sadece deneme amaçlıdır.

---

## 🛠️ Özellikler

- 📅 Rastgele tarih oluşturma
- 🔢 Otomatik fatura numarası üretimi
- 🛒 Rasgele ürün/fiyat kombinasyonları
- 🧾 PDF formatında çıktı
- ❌ Üzerinde kırmızı "GEÇERSİZDİR" damgası
- 💻 CLI üzerinden tek komutla fatura üretimi

---

## 🔧 Kurulum

Python 3.x yüklü olduğundan emin olun.

```bash
git clone https://github.com/kullaniciadi/sahtekar.git
cd sahtekar
pip install reportlab
python generate_invoice.py
```

Çalıştırıldığında bulunduğunuz dizine fatura_XXXXXX.pdf isminde sahte bir fatura oluşturur.

## 📝 Notlar

Bu yazılım gerçek fatura düzenlemek için kullanılmamalıdır.
Tamamen deneysel ve simülasyon amaçlı yazılmıştır.
Üretilen belgeler yasal olarak hiçbir geçerlilik taşımaz.