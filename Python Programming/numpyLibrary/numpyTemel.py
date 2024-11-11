# NumPy Nedir?
# NumPy, Python'da bilimsel hesaplamalar yapmak için kullanılan bir kütüphanedir. Çok boyutlu diziler ve matrisler üzerinde çalışmamızı sağlar ve yüksek düzeyde matematiksel fonksiyonlar içerir.

# NumPy ile Dizi (Array) Oluşturma
# NumPy’de diziler Python listelerine benzer ancak matematiksel işlemleri daha hızlı ve verimli gerçekleştirir.

import numpy as np
# Listeyi NumPy dizisine çevirme
dizi = np.array([1, 2, 3, 4, 5])
print(dizi)


# Özel Diziler Oluşturma
# NumPy, sıfır veya bir ile dolu diziler ve rastgele sayılar içeren diziler gibi özel diziler oluşturmayı kolaylaştırır.

# Sıfır ve bir dolu diziler
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
random_values = np.random.rand(2, 3)

# Array Manipülasyonları
# NumPy dizileri üzerinde şekil değiştirme, birleştirme ve ayırma gibi işlemler yapılabilir.

# reshape: Dizinin şeklini yeniden tanımlar.
# concatenate: İki veya daha fazla diziyi birleştirir.
# split: Diziyi belirli noktalardan böler.

a = np.array([1, 2, 3, 4, 5, 6])
reshaped = a.reshape(2, 3)  # 2x3 şekline dönüştürür
print(reshaped)

# Indexleme ve Dilimleme
# Dizilerde elemanlara erişmek ve belirli bölümleri almak için dilimleme ve koşullu dilimleme yapılabilir.

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0, 0])  # İlk eleman
print(b[:, 1])  # İkinci sütundaki tüm elemanlar

# Öznitelikler ve İşlemler
# ndim: Dizinin boyut sayısını verir.
# shape: Dizinin şeklini döndürür.
# size: Dizideki toplam eleman sayısını verir.

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)  # (2, 3)


# Yayınlama (Broadcasting)
# Farklı boyutlardaki diziler üzerinde eleman eleman işlemler yapılabilir.

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)  # Her satırda b ile toplama


# Aritmetik ve Matematiksel İşlemler
# NumPy, aritmetik işlemler yanında üstel, logaritmik ve trigonometrik fonksiyonları da destekler.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # Toplama
print(np.sin(a))  # Sinüs


# İstatistiksel Fonksiyonlar
# Ortalama, medyan ve standart sapma gibi istatistiksel fonksiyonlarla veri analizi yapılabilir.

a = np.array([1, 2, 3, 4, 5])
print(np.mean(a))  # Ortalama
print(np.std(a))   # Standart sapma


# Lineer Cebir Fonksiyonları
# dot: Vektör veya matris çarpımı.
# inv: Matrisin tersini hesaplar.
# solve: Lineer denklem sistemini çözer.

a = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
print(np.linalg.solve(a, b))  # Lineer denklem çözümü
