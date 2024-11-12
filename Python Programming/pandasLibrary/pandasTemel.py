# Pandas Kütüphanesi Kapsamlı Özeti
# Pandas, veri manipülasyonu ve analizi için Python'da yaygın olarak kullanılan güçlü bir kütüphanedir. DataFrame ve Series veri yapılarıyla veri işleme işlemlerinde esneklik sağlar.


# Veri Yükleme ve Kaydetme
# Pandas, farklı kaynaklardan veri okuma ve dosyalara yazma işlemleri sunar.

import pandas as pd

# Dosyadan veri yükleme
df_csv = pd.read_csv('data.csv')     # CSV dosyası
df_excel = pd.read_excel('data.xlsx') # Excel dosyası
df_json = pd.read_json('data.json')   # JSON dosyası

# Veri kaydetme
df_csv.to_csv('output.csv', index=False)
df_excel.to_excel('output.xlsx', index=False)
df_json.to_json('output.json')


# DataFrame Temel İşlemleri
# df.head(n): İlk n satırı görüntüler.
# df.tail(n): Son n satırı görüntüler.
# df.info(): Veri hakkında bilgi verir.
# df.describe(): Sayısal sütunların temel istatistiklerini döner.
# df.shape: Satır ve sütun sayısını gösterir.


# Kolonlarla Çalışma
# Yeni kolon eklemek veya mevcut bir kolonu değiştirmek:

df['yeni_kolon'] = df['kolon1'] * 2


# Kolon seçme:

df['kolon1']   # Tek bir kolon seçme
df[['kolon1', 'kolon2']]  # Birden fazla kolon seçme


# Veri Manipülasyonu
# Veri Tipi Dönüşümleri:

df['kolon1'] = df['kolon1'].astype(float)

# Filtreleme:

df[df['kolon1'] > 10]  # 'kolon1' değeri 10'dan büyük olan satırları seç

# Eksik ve Tekrarlayan Veriler:

df.fillna(0)          # Eksik değerleri 0 ile doldur
df.dropna()           # Eksik satırları sil
df.drop_duplicates()  # Tekrarlayan satırları sil


# Sıralama:

df.sort_values(by='kolon1', ascending=False)  # Kolona göre sıralama


# Gruplama ve Toplama İşlemleri
# Pandas gruplama işlemlerini groupby() ile yapar ve çeşitli özet fonksiyonlarını kullanır.

# Ortalama değer
df.groupby('kategori_kolon')['deger_kolon'].mean()

# Toplam değer
df.groupby('kategori_kolon')['deger_kolon'].sum()


# Veri Birleştirme
# pd.merge(): İki veri setini ortak bir kolona göre birleştirir.
# pd.concat(): Aynı veya farklı veri setlerini üst üste veya yan yana birleştirir.

df_merged = pd.merge(df1, df2, on='ortak_kolon')
df_concat = pd.concat([df1, df2], axis=1)  # Yan yana birleştirme


# Görselleştirme
# Pandas, hızlı görselleştirme için plot() fonksiyonunu sunar.

df['kolon'].plot(kind='hist')    # Histogram
df.plot(kind='scatter', x='x', y='y')  # Dağılım grafiği
df.plot(kind='box')               # Kutu grafiği
