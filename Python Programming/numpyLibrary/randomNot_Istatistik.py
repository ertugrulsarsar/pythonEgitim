# Bu uygulama, rastgele üretilen öğrenci notlarından oluşan bir veri seti oluşturur ve bu veriler üzerinde çeşitli istatistiksel analizler yapar.

import numpy as np

# 100 öğrencinin 5 farklı sınav notunu rastgele oluşturma (notlar 0-100 arasında)
np.random.seed(0)  # Sonuçların aynı kalması için sabit tohum değeri
ogrenci_notlari = np.random.randint(0, 101, (100, 5))

# Her öğrenci için ortalama not hesaplama
ortalama_notlar = np.mean(ogrenci_notlari, axis=1)
print("Öğrenci Ortalama Notları:", ortalama_notlar)

# Ortalama notlara göre sınıfın genel ortalaması ve medyanı
sinif_ortalamasi = np.mean(ortalama_notlar)
sinif_medyan = np.median(ortalama_notlar)
print("Sınıf Ortalaması:", sinif_ortalamasi)
print("Sınıf Medyanı:", sinif_medyan)

# Sınıfın standart sapması ve en yüksek notu
standart_sapma = np.std(ortalama_notlar)
en_yuksek_not = np.max(ogrenci_notlari)
print("Sınıf Standart Sapması:", standart_sapma)
print("Sınıfta Alınan En Yüksek Not:", en_yuksek_not)
