# ort=0 
# Y1 = 20
# Y2 = 30

# ort = (Y1+Y2)/2

# print(ort)

# Y1= int(input("Birinci Notu Giriniz: "))
# Y2= int(input("İkinci Notu Giriniz: "))

# ort = 0
# ort = (Y1 + Y2)/2

# print (ort)


# dogum_tarihi = int(input("Dogum Yılınızı Giriniz:"))

# yas= 2024-dogum_tarihi

# print("yasınız: ", yas)

# 8>2 and 10 >10 or 400 > 300
# print(8>2 and  10 >10 or 400 >300) 

# Not = int(input("Notunuzu Giriniz: "))

# if Not >= 50:
#     alinan_fazla_puan = Not - 50
#     print(f"Notunuz Geçmek için Yeterlidir: {Not} ")
#     print(f"Alınan Fazla Puan: {alinan_fazla_puan} ")
# else:
#     gerekli_puan = 50 - Not
#     print(f"Notunuz Geçmek için yeterli değildir: {Not}")
#     print(f"Geçebilmek için almanız gereken ek puan: {gerekli_puan}")

# user = input("Kullancı Adınızı Giriniz:")
# sifre = int(input("Sifre Giriniz:"))


# if user =="admin" and sifre == 1234:
#     isim = "baha sezerer "
#     print(f"Giriş Yapıldı Hoşgeldiniz {isim}")
# else:
#     yetki = "Kullancıya Mesaj İletildi"
#     print(f"Yanlış Kullancı adı veya Şifre Girdiniz {yetki}")
# for a in range (1,101,3):
#     print(f"sayılar = {a}")

# for a in range(1,31):
#     if (a%2 ==1 ):
#         print(a)

# while True:
#     a = 1
#     print("Çıkış için sıfıra bas")
#     while a != 0:
#         a = int(input("Sayı giriniz: "))
#         if a != 0:
#             print("Sayının karesi ==", a * a)
    
#     tekrar = input("Tekrar başlamak ister misiniz? (Evet için 'e', Hayır için 'h' yazın): ").lower()
    
#     if tekrar == 'h':
#         emin_misin = input("Emin misiniz? (Evet için 'e', Hayır için 'h' yazın): ").lower()
#         if emin_misin == 'e':
#             print("Güle güle!")
#             break
#         else:
#             print("Tekrar başlatılıyor...")

# for A in range(1,11):
#     for B in range(1,11):
#         print(A,"*",B,"=", A*B)
#     print("\n")   

# sifre = 1234 
# kullanici_adi = "baha"

# ad = input("kullancı adı giriniz:")
# if kullanici_adi == ad:  
#     password = int(input ("sifre giriniz:"))
#     if password == sifre:
#         print("ve sifre doğru")

#     else:
#         print("yanlış")
# else:
#     print("kullancı ismi yanlıs")

# class Araba:
#     def __init__(self, marka,model,renk): #METOD ataması
#         self.marka = marka  # Başlangıçta markayı atıyoruz
#         self.model = model
#         self.renk = renk
    
#     def metot(self): #METOD işelmler
#         self.marka = "Mercedes"  # Markayı değiştiriyoruz
#         return self.marka  # Yeni markayı döndürüyoruz

    
# araba1 = Araba("BMW",2020,"kirmizi") # NESNEMİZ
# print(araba1.marka)  # Çıktı: BMW
# print(araba1.model)  # Çıktı: BMW
# print(araba1.renk)  # Çıktı: BMW

# import random
# skor= 5
# sayi =random.randint(1,6)
# tahmin = int(input(f"sayıyı tahmin et: "))

# while True:
#     if sayi ==tahmin:
#         print(f"kazandınız Skorunuz: {skor} ")
#         break
#     else:
#         print(f"olmadı: Skorunuz: {skor} ")
#         skor-=1
#         tahmin=int(input("tahmin et: "))

# import random
# Liste = ["Taş","Kağıt","Makas"]
# pc= random.choice(Liste)

# tahmin= input("Taş-Kağıt-Makas").capitalize()

# print("bilgisayar", pc, "seçti")
# print("sen",tahmin,"seçtin")


# while True:
#     if pc==tahmin:
#         print("beraber")

#     if pc =="Kağıt"and tahmin=="Taş":
#         print("kaybettin")
#     if pc =="Taş"and tahmin=="Makas":
#         print("kaybettin")
#     if pc =="Makas"and tahmin=="Kağıt":
#         print("kaybettin")
    
#     if pc =="Kağıt"and tahmin=="Makas":
#         print("kazandın")
#     if pc =="Taş"and tahmin=="Kağıt":
#         print("kazandın")
#     if pc =="Makas"and tahmin=="Taş":
#         print("kazandın")
#         break

# from turtle import *

# # Ekran ayarları
# ekran = Screen()
# ekran.title("Fare ile Çizim ve Kalemi Kaldığı Yerden Devam Ettir")
# ekran.setup(width=600, height=600)  # Pencere boyutunu ayarla

# # Kalem ayarları
# kalem = Turtle()
# kalem.shape("turtle")
# kalem.pensize(3)
# kalem.speed(0)

# # Çizim yapma fonksiyonu
# def KalemleCiz(x, y):
#     if kalem.isdown():  # Kalem aşağıda ise çizim yapılır
#         kalem.goto(x, y)    # Kalemi fare konumuna götür
#     else:
#         kalem.penup()  # Kalemi kaldır

# # Fare tıklaması ile kalem durumunu değiştirme
# def FareTıklama(x, y):
#     if kalem.isdown():
#         kalem.penup()  # Kalemi kaldır
#     else:
#         kalem.pendown()  # Kalemi indir

# # Çizimi temizleme fonksiyonu
# def CizimiSil():
#     kalem.clear()

# # Fare ile çizim yapmak için kalemi indir
# kalem.pendown()

# # Fare hareketini dinleyerek çizim yap
# kalem.ondrag(KalemleCiz)

# # Fare tıklaması ile kalemi aktif veya pasif hale getir
# ekran.onclick(FareTıklama)

# # Klavye dinleyicisi (Ctrl+Z gibi z tuşu ile çizimi temizler)
# def KlavyeDinleyici():
#     ekran.listen()
#     ekran.onkey(CizimiSil, "z")  # 'z' tuşuna basıldığında temizle

# # Klavye dinleyicisini başlat
# KlavyeDinleyici()

# # Ekranı açık tut
# ekran.mainloop()


# from turtle import *

# # Ekranı ve kalemi ayarla
# w = Screen()
# w.setup(700, 700)


# kalem = Turtle()
# kalem.shape("turtle")
# kalem.pensize(4)

# # Fonksiyonlar
# def solaDon():
#     kalem.left(90)
   

# def sagDon():
#     kalem.right(90)
 

# def ileri():
#     kalem.forward(10)
  

# def geri():
#     kalem.backward(10)
  

# # Klavye olayları
# w.onkeypress(solaDon, "Left")
# w.onkeypress(sagDon, "Right")
# w.onkeypress(ileri, "Up")
# w.onkeypress(geri, "Down")

# # Dinlemeyi başlat
# w.listen()

# # Pencereyi açık tut
# w.mainloop()

# from turtle import *
# import time

# # Ekran ayarları
# w = Screen()
# w.setup(700, 700)
# w.title("TRAFİK IŞIĞI")

# # Kalem ayarları
# penup()
# goto(0, 180)
# pendown()
# pensize(4)

# # Dikdörtgen çerçeve oluşturma
# for i in range(2):
#     forward(80)
#     right(90)
#     forward(220)
#     right(90)

# # Işıklar için fonksiyonlar
# def kirmizi():
#     penup()
#     goto(40, 140)
#     fillcolor("red")
#     begin_fill()
#     shape("circle")
#     shapesize(3)
#     end_fill()

# def sari():
#     penup()
#     goto(40, 70)
#     fillcolor("yellow")
#     begin_fill()
#     shape("circle")
#     shapesize(3)
#     end_fill()

# def yesil():
#     penup()
#     goto(40, 0)
#     fillcolor("green")
#     begin_fill()
#     shape("circle")
#     shapesize(3)
#     end_fill()

# # Döngüden çıkma kontrolü
# exit_flag = False

# def exit_program():
#     global exit_flag
#     exit_flag = True

# # Klavye olayları
# w.onkeypress(exit_program, "q")  # 'q' tuşuna basıldığında döngüyü durdur

# w.listen()

# # Renk döngüsü
# while not exit_flag:
#     yesil()
#     time.sleep(3)
#     if exit_flag:
#         break

#     sari()
#     time.sleep(3)
#     if exit_flag:
#         break

#     kirmizi()
#     time.sleep(2)
#     if exit_flag:
#         break

# # Pencereyi açık tut
# w.mainloop()

import random
import turtle
import time
delay =0.15

 
w= turtle.Screen()
w.title('Yılan Oyunu')
w.bgcolor('lightgreen')
w.setup(width=600, height=600)
w.tracer(0)
 
k = turtle.Turtle()
k.speed(0)
k.shape("square")
k.color("black")
k.penup()
k.goto(0, 100)
k.direction = "stop"
 
yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()
yemek.shapesize(0.80, 0.80)
yemek.goto(0, 0)
 
kuyruklar = []
puan = 0
 
yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("white")
yaz.penup()
yaz.hideturtle()
yaz.goto(0, 260)
yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
 
def move():
    if k.direction == "up":
        y = k.ycor()
        k.sety(y + 20)
    if k.direction == "down":
        y = k.ycor()
        k.sety(y - 20)
    if k.direction == "right":
        x = k.xcor()
        k.setx(x + 20)
    if k.direction == "left":
        x = k.xcor()
        k.setx(x - 20)
 
def go_up():
    if k.direction != "down":
        k.direction = "up"
def go_down():
    if k.direction != "up":
        k.direction = "down"
def go_right():
    if k.direction != "left":
        k.direction = "right"
def go_left():
    if k.direction != "right":
        k.direction = "left"
 
w.listen()
w.onkey(go_up, "Up")
w.onkey(go_down, "Down")
w.onkey(go_right, "Right")
w.onkey(go_left, "Left")
 
while True:
    w.update()
 
    if k.xcor() > 300 or k.xcor() < -300 or k.ycor() > 300 or k.ycor() < -300:
        time.sleep(1)
        k.goto(0, 0)
        k.direction = "stop"
 
        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)
        kuyruklar = []
 
        puan = 0
        delay = 0.1
 
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
 
    if k.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)
 
        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("white")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)
 
        delay -= 0.001
 
        puan = puan + 10
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
 
    for index in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[index - 1].xcor()
        y = kuyruklar[index - 1].ycor()
        kuyruklar[index].goto(x, y)
 
    if len(kuyruklar) > 0:
        x = k.xcor()
        y = k.ycor()
        kuyruklar[0].goto(x, y)
 
    move()
 
    for segment in kuyruklar:
        if segment.distance(k) < 20:
            time.sleep(1)
            k.goto(0, 0)
            k.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar = []
            puan = 0
            yaz.clear()
            yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
            hiz = 0.15
 
    time.sleep(delay)


