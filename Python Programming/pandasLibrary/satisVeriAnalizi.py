import pandas as pd

# Örnek satış verisi
veri = {
    'sehir': ['İstanbul', 'Ankara', 'İzmir', 'Antalya', 'Bursa'],
    'urun_1': [150, 200, 180, 130, 170],
    'urun_2': [220, 180, 160, 210, 150]
}
df = pd.DataFrame(veri)

# Toplam satış miktarını hesaplayın
df['toplam_satis'] = df[['urun_1', 'urun_2']].sum(axis=1)

# En yüksek satış miktarını ve şehrini bulun
max_satis = df['toplam_satis'].max()
en_yuksek_satis_sehri = df[df['toplam_satis'] == max_satis]['sehir'].values[0]

print(f"En yüksek satış miktarı {max_satis} ile {en_yuksek_satis_sehri} şehrinde gerçekleşti.")
