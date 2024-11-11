# Öğrencilerin sınav ve ödev notlarından hesaplanan ortalamalarına göre geçme durumu belirlenir.

import numpy as np

# Öğrenci verileri: [Ödev, Sınav1, Sınav2, Final]
ogrenci_notlari = np.array([[80, 70, 90, 60],
                            [50, 60, 70, 75],
                            [85, 90, 95, 80]])

# Ağırlıklar
weights = np.array([0.2, 0.2, 0.2, 0.4])

# Ortalama hesaplama
ortalama = np.dot(ogrenci_notlari, weights)
print("Ortalama Notlar:", ortalama)

# Geçme durumu
gecenler = ortalama >= 60
print("Geçme Durumu:", gecenler)
