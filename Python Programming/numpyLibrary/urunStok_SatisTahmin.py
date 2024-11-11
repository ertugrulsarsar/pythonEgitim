# Bu uygulama, 50 farklı ürün için rastgele stok miktarları ve günlük satış tahminleri oluşturur. Satış tahminlerine göre stok bitiş süreleri hesaplanır.

import numpy as np

# 50 farklı ürün için stok miktarları (100 ile 500 arasında rastgele değerler)
stok_miktarlari = np.random.randint(100, 501, 50)

# Her ürün için günlük satış tahmini (1 ile 20 arasında rastgele değerler)
gunluk_satis_tahminleri = np.random.randint(1, 21, 50)

# Stok bitiş süresini (gün olarak) hesapla
stok_bitis_sureleri = stok_miktarlari / gunluk_satis_tahminleri
stok_bitis_sureleri = np.ceil(stok_bitis_sureleri)  # Gün sayısını tam sayı olarak almak için

# Ortalama stok bitiş süresi ve en kısa stok bitiş süresi
ortalama_stok_bitis = np.mean(stok_bitis_sureleri)
en_kisa_stok_bitis = np.min(stok_bitis_sureleri)
print("Ortalama Stok Bitiş Süresi (gün):", ortalama_stok_bitis)
print("En Kısa Stok Bitiş Süresi (gün):", en_kisa_stok_bitis)
