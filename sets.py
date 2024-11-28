user_name = "baha"

e_mail = "bahasezerer3"

Parola = 12345

girilen_bilgi = input( "user ya da mail: " )
girilen_sifre = input("sifre giriniz: ")


giris = (user_name== girilen_bilgi) or (e_mail == e_mail) and (Parola == girilen_sifre)

print (giris)