print("### Değer Değiştirme Programı ###")
a = int(input("Lütfen birinci sayıyı girin: "))
b = int(input("Lütfen ikinci sayıyı girin: "))
print("\nBirinci değer: {}\nİkinci değer: {}".format(a,b))
a,b = b,a
print("\nDeğerler değiştiriliyor...")
print("\nDeğiştirildikten sonra birinci değer: {}\nDeğiştirildikten sonra ikinci değer: {}".format(a,b))
