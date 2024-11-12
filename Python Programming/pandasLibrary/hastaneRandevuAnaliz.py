import pandas as pd
import numpy as np

# Randevu verisi
np.random.seed(1)
hastalar = pd.DataFrame({
    'isim': [f'Hasta {i+1}' for i in range(50)],
    'yas': np.random.randint(18, 80, 50),
    'randevu_sayisi': np.random.randint(1, 10, 50)
})

# Yaş grubuna göre randevu sayısını gruplama
hastalar['yas_grubu'] = pd.cut(hastalar['yas'], bins=[18, 30, 45, 60, 80], labels=['18-30', '30-45', '45-60', '60-80'])
randevu_analizi = hastalar.groupby('yas_grubu')['randevu_sayisi'].sum()

print("Yaş grubuna göre toplam randevu sayısı:")
print(randevu_analizi)
