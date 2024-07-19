print("### Hipotenüs Hesaplama ###")
kenar_1 = float(input("\nLütfen birinci kenarın uzunluğunu yazınız: "))
kenar_2 = float(input("Lütfen ikinci kenarın uzunluğunu yazınız: "))
hipotenus = (kenar_1**2+kenar_2**2)**0.5
print("\nGirilen kenar değerlerine göre hiponetüs uzunluğu: {:.3f}".format(hipotenus))