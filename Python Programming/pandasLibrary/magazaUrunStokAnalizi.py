import pandas as pd
import numpy as np

# Ürün verisi
np.random.seed(2)
urunler = pd.DataFrame({
    'urun': [f'Urun {i+1}' for i in range(15)],
    'stok': np.random.randint(5, 30, 15),
    'gunluk_satis': np.random.randint(1, 5, 15)
})

# Stok yetersizliği analizini yapma
urunler['stok_yeterlilik'] = np.ceil(urunler['stok'] / urunler['gunluk_satis'])
dusuk_stok_urunler = urunler[urunler['stok_yeterlilik'] < 5]

print("Stok yetersizliği olan ürünler:")
print(dusuk_stok_urunler[['urun', 'stok', 'stok_yeterlilik']])
