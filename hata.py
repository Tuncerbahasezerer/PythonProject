def yas_kontrol(yas):
    if yas < 18:
        raise ValueError("Yaş 18'den küçük olamaz!")
    print("Yaş kabul edildi:", yas)

# Kullanım:
yas_kontrol(13)  # ValueError: Yaş 18'den küçük olamaz!