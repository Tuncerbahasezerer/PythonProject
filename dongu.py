hesaplar = [
    {
           "ad" : "baha sezerer",
           "hesapNo" : "12345",
           "bakiye" : 20000,
           "ekHesap" : 5000,     
           "username" : "bahasezerer",
           "password" : "1234"
    },
    {
           "ad" : "ahmet bal",
           "hesapNo" : "123456",
           "bakiye" : 300000,
           "ekHesap" : 10000,     
           "username" : "ahmetbal",
           "password" : "2222"
    },
    {
           "ad" : "vedat sezerer",
           "hesapNo" : "1234578",
           "bakiye" : 400000,
           "ekHesap" : 20000,     
           "username" : "vedatsezerer",
           "password" : "3333"
    },   
]

def menu(hesap):
    print("\n")
    print(f"merhaba, {hesap["ad"]}" )
    print("1- bakiye sorgulama")
    print("2-para çekme")
    print("3-para yatırma")

    islem= input("Yapmak İstediğiniz İşlem: ")

    if islem == "1": 
        bakiyeSorgula(hesap)
    elif islem =="2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    else:
        print("yanlış seçim")
    
    menu(hesap)

def bakiyeSorgula(hesap):
    print(f"bakiye: {hesap["bakiye"]}")
    print(f"ek bakiye: {hesap["ekHesap"]}")

def paraCekme(hesap):
    miktar = float(input("çekmek istediğiniz miktar: "))
    
    if hesap["bakiye"] >=miktar:
        hesap["bakiye"] -=miktar
        print("paranızı alablirsiniz. ")
    else:
        toplam = hesap["bakiye"] + hesap ["ekHesap"]
        
        if toplam >=miktar:
            
            ekHesapKullanimIzni = input("ek hesap izni verilsin mi ? (e/h)")
            
            if ekHesapKullanimIzni== "e":
                kullanilacakMiktar = miktar - hesap ["bakiye"]
                hesap["bakiye"]= 0
                hesap["ekHesap"] -=kullanilacakMiktar
                print("paranızı alabilirsiniz")
           
            else:
                print("üzgünüz bakiyeniz yetersiz")
       
        else:
                print("üzgünüz bakiyeniz yetersiz")

def paraYatirma(hesap):
    
    miktar = float(input("yatırmak istediğiniz miktar: "))
    
    if  miktar <1:
        print("miktar çok düşük tekrar deneyiniz ! ")
    
    elif hesap["bakiye"] + miktar:

        print(f"paranız yatırıldı toplam bakiye {hesap ["bakiye"]+ miktar }")



        





def login():
    username = input("username: ")
    password = input("password: ")
    isloggedIn =False


    for hesap in hesaplar:
        if hesap ["username"] == username and hesap["password"] == password:
            isloggedIn =True
            menu(hesap)
            break
    if not(isloggedIn):
        print("username ya da parola yanlıştır.") 

login()