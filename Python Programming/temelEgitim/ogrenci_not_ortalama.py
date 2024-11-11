# Kullanıcıdan ara sınav ve final notları alınarak ortalama hesaplanır. Ortalama 50 ve üzerindeyse geçer, aksi halde kalır.

def not_hesapla():
    as_notu = float(input("Ara Sınav notunu giriniz: "))
    fn_notu = float(input("Final notunu giriniz: "))
    ortalama = (as_notu * 0.4) + (fn_notu * 0.6)
    
    print(f"Ortalamanız: {ortalama}")
    if ortalama >= 50:
        print("Geçtiniz!")
    else:
        print("Kaldınız.")

not_hesapla()