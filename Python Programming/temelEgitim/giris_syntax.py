# Python'a Giriş ve Temel Söz Dizimi
# Kod Yazma Kuralları ve İlk Program: Python’da girintileme (indentation) yapısı, satır satır yazma ve print() kullanarak ilk program.
# REPL (Read-Evaluate-Print Loop): Python shell ile etkileşimli olarak kod çalıştırma ve girdileri değerlendirme.

print("Merhaba Dünya!")
input_data = input("Bir sayı girin: ")
processed_data = int(input_data) * 2
print(f"İşlenen verinin sonucu: {processed_data}")


# Değişkenler ve Veri Türleri
# Değişken Tanımlama ve Atama: Python'da değişkenlerin nasıl tanımlandığı, veri türleri (int, float, str, bool).
# Koleksiyon Veri Türleri: Liste, demet, sözlük, ve kümeler.
# Veri Tipi Dönüşümleri: int(), float(), str() gibi veri türleri arasında dönüşümler.

yas = 25
isim = "Ali"
pi_sayisi = 3.14
dogru_mu = True
sehirler = ["Ankara", "İstanbul", "İzmir"]


# Operatörler
# Aritmetik Operatörler: +, -, *, /, //, %, **
# Karşılaştırma Operatörleri: ==, !=, <, >, <=, >=
# Mantıksal Operatörler: and, or, not
# Atama Operatörleri: =, +=, -=, *=, /=

a = 10
b = 3
print(a + b)
print(a ** b)
print(a == b)
print(a > b and b > 0)


# Python Koleksiyonları (List, Tuple, Set, Dictionary)
# Listeler: Liste oluşturma, eleman ekleme (append), silme (remove), sort ve reverse metodları.
# Tuple (Demetler): Sabit veri yapıları ve count, index gibi metodlar.
# Set (Kümeler): Tekrarsız elemanlardan oluşur, union, intersection, difference gibi küme işlemleri.
# Dictionary (Sözlük): Anahtar-değer çiftleri, get, items, update gibi metodlarla veri yönetimi.

meyveler = ["elma", "muz", "çilek"]
meyveler.append("portakal")
ogrenci = {"ad": "Ali", "yas": 25, "bolum": "Bilgisayar"}
renkler = {"kırmızı", "mavi", "yeşil"}



# Koşul İfadeleri ve Karar Yapıları
# if, elif, else Yapıları: Şartlı durumlar ve farklı koşullara göre işlem yapma.
# Ternary Koşul İfadesi: Tek satırda koşul ifadeleri (min_value = a if a < b else b).
# İç İçe Koşullar ve Şartlı Yapılar: Karar yapıları içinde başka kararlar alma.

yas = int(input("Yaşınızı giriniz: "))
if yas < 18:
    print("Reşit değilsiniz.")
elif yas == 18:
    print("Henüz yeni reşitsiniz.")
else:
    print("Reşitsiniz.")



# Döngüler (For ve While)
# For Döngüsü: range() fonksiyonu ile döngü kontrolü, liste ve sözlüklerde dolaşma.
# While Döngüsü: Koşul sağlandığı sürece döngüde kalma.
# break ve continue Kullanımı: Döngüyü kırma veya döngünün bir adımını atlama.

for i in range(5):
    print(i)

x = 0
while x < 5:
    print(x)
    x += 1



# List Comprehension (Liste Üretimi)
# Liste, sözlük ve set comprehension ile kısa ve etkili veri yapıları oluşturma.
# Koşullu List Comprehension

kareler = [x ** 2 for x in range(10)]
cift_sayilar = [x for x in range(10) if x % 2 == 0]



# Fonksiyonlar
# Fonksiyon Tanımlama: def ile fonksiyon oluşturma.
# Varsayılan Parametreler: def greet(name="Ziyaretçi")
# Birden Fazla Geri Dönüş Değeri: return max(numbers), min(numbers)
# Belirsiz Sayıda Parametre (*args, **kwargs): Esnek parametreli fonksiyonlar.
# Lambda Fonksiyonlar: Tek satırlık anonim fonksiyonlar.

def toplama(a, b):
    return a + b
print(toplama(2, 3))

kare_al = lambda x: x ** 2
print(kare_al(5))


# Modüller ve Kütüphaneler
# Modül İmport Etme: import random, import math
# random ve math Modüllerinin Kullanımı: Rastgele sayı üretme, matematiksel işlemler.

import random
rastgele_sayi = random.randint(1, 100)
print(rastgele_sayi)
