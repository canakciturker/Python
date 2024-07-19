print("### Araba Yakıt Sarfiyatı Hesaplama ###")
sehiriciyakit = float(input("Aracınızın şehir içi kaç litre yaktığını yazınız: "))
sehirdisiyakit = float(input("Aracınızın şehir dışı kaç litre yaktığını yazınız: "))
litrefiyat = float(input("Güncel litre fiyatını yazınız: "))
kilometre = float(input("Kaç kilometre yol alacağınızı yazınız: "))
yakitsarfiyatısehirici = sehiriciyakit*litrefiyat*kilometre/100
yakitsarfiyatısehirdisi = sehirdisiyakit*litrefiyat*kilometre/100
print("\nArabanızın şehir içi ortalama yakıt sarfiyatı şu şekildedir: {}\nArabanızın şehir dışı ortalama yakıt sarfiyatı şu şekildedir: {}".format(yakitsarfiyatısehirici,yakitsarfiyatısehirdisi) )