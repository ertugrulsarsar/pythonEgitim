import pandas as pd
import numpy as np

# Rastgele öğrenci notları oluşturma
np.random.seed(0)
ogrenci_notlari = pd.DataFrame({
    'isim': [f'Ogrenci {i+1}' for i in range(20)],
    'sinav1': np.random.randint(50, 100, 20),
    'sinav2': np.random.randint(50, 100, 20),
    'final': np.random.randint(50, 100, 20)
})

# Ortalama hesaplayarak geçme-kalma durumunu belirleme
ogrenci_notlari['ortalama'] = ogrenci_notlari[['sinav1', 'sinav2', 'final']].mean(axis=1)
ogrenci_notlari['durum'] = np.where(ogrenci_notlari['ortalama'] >= 60, 'Geçti', 'Kaldı')

print(ogrenci_notlari[['isim', 'ortalama', 'durum']])
