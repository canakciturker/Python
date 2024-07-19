print("###Oyuncu Kaydetme Programı###\n")
ad = input("Oyuncu Adı: ")
soyad = input("Oyuncunun Soyadı: ")
takım = input("Oyuncun Takımı: ")

bilgiler  = [ad,soyad,takım]
print("\nBilgiler Kaydediliyor...\n")
print("Oyuncu adı: {}\nOyuncu soyadı: {}\nOyuncu takımı: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))
print("\n.....Bilgiler Kaydedildi.....")
