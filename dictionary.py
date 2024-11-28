ogrenciler = {

101: {
     "ad":"baha",
     "soyad" : "sezerer",
     "DogumYili" : 2002,
     "Notlar" : (40,80,90)
},

102: {
     "ad":"baha2",
     "soyad" : "sezerer2",
     "DogumYili" : 2005,
     "Notlar" : (200,80,90)
},

103: {
     "ad":"baha3",
     "soyad" : "sezerer3",
     "DogumYili" : 2012,
     "Notlar" : (20000,80,90)
},

}
ogrenciNo = int(input("öğrenci no: "))

ogrenci= ogrenciler[ogrenciNo]

ortalama =(ogrenci["Notlar"][0]+ ogrenci["Notlar"][1]+ogrenci["Notlar"][2])

print (f"{ogrenciNo} numaralı {ogrenci["ad"]} {ogrenci["soyad"]} ismindeki öğrencinin yaşı {2024- ogrenci["DogumYili"]} ve not ortalamsı {ortalama}. ")
