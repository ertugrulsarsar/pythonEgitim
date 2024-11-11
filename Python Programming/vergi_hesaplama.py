# Kullanıcının gelirine göre vergi oranları uygulanır ve toplam vergi hesaplanır.

def vergi_hesapla():
    gelir = float(input("Yıllık gelirinizi giriniz: "))
    asgari_ucret = 17002
    vergi = 0
    
    if gelir <= asgari_ucret:
        vergi = 0
    elif gelir <= 50000:
        vergi = (gelir - asgari_ucret) * 0.15
    elif gelir <= 100000:
        vergi = (50000 - asgari_ucret) * 0.15 + (gelir - 50000) * 0.20
    else:
        vergi = (50000 - asgari_ucret) * 0.15 + (100000 - 50000) * 0.20 + (gelir - 100000) * 0.30
    
    print(f"Toplam verginiz: {vergi} TL")

vergi_hesapla()
