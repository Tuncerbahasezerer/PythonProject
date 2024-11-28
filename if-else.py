benzin = 39.35
dizel = 41.71
lpg = 20.28 

 
toplamYakitUcreti = 0 
ortalamaYakitTüketimi = float(input("100'km deki ortalama yakit tüketimi: "))
gidilecek_yol = float(input("gidilen mesafe: "))
yakit_tipi = input("yakit tipi: ")

toplamYakitTuketimi= gidilecek_yol * (ortalamaYakitTüketimi / 100)

if( yakit_tipi == "benzin"):
    toplamYakitUcreti = benzin* toplamYakitTuketimi

elif(yakit_tipi == "dizel"):    
    toplamYakitUcreti = dizel* toplamYakitTuketimi

elif(yakit_tipi == "lpg"):    
    toplamYakitUcreti = lpg* toplamYakitTuketimi

else:
    print("yanlis deger girildi")

if(toplamYakitUcreti !=0):
    print(toplamYakitUcreti)

else: 
    print("yola çıkılmamış :) ")
