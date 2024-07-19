"""
2. Dereceden bir bilinmeyenli denklemin kökünü bulma
Denklem: ax^2 + bx + c
Deltayı Hesaplama: b^2 - 4ac
Birinci kök: (-b+Delta**0,5)/(2*a)
İkinci kök: (-b-Delta**0,5)/(2*a)
"""
print("### Kök Bulma Programı ###")
a = int(input("Lütfen denklemin a değerini giriniz: "))
b = int(input("Lütfen denklemin b değerini giriniz: "))
c = int(input("Lütfen denklemin c değerini giriniz: "))
degiskenler = [a,b,c]
print("\nDenkleminiz şu şekilde: {}x^2 + {}x + {}".format(a,b,c))
delta = b**2 - 4*a*c
print("{} ise denklemin deltasıdır.".format(delta))
x_1 = (-b+delta**0.5)/(2*a)
x_2 = (-b-delta**0.5)/(2*a)
print("\n{} ve {} denklemin kökleridir".format(x_1,x_2))