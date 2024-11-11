# Kullanıcıdan çekmek istediği tutar alınır ve bakiye kontrolü yapılır. Yeterli bakiye varsa para çekilir, yoksa yetersiz bakiye uyarısı verilir.

def atm_uygulamasi():
    bakiye = 1000  # Mevcut bakiye
    print(f"Bakiyeniz: {bakiye} TL")
    
    cekilecek_tutar = float(input("Çekmek istediğiniz tutarı giriniz: "))
    if cekilecek_tutar > bakiye:
        print("Yetersiz bakiye.")
    else:
        bakiye -= cekilecek_tutar
        print(f"Başarıyla {cekilecek_tutar} TL çektiniz.")
        print(f"Güncel bakiyeniz: {bakiye} TL")

atm_uygulamasi()
