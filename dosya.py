class BankaHesabi:
    def __init__(self, hesapismi):
        self.hesapismi = hesapismi
        self.bakiye = 0.0
    
    def get_bakiye(self): 
        return self.bakiye

    def paraYatir(self, miktar):
        self.bakiye +=miktar
        return self.bakiye
    
    def paraCek(self,miktar):
        self.bakiye -=miktar
        return self.bakiye

hesap = BankaHesabi ("baha sezerer")
hesap.paraYatir(1000)
print(hesap.get_bakiye())
print(hesap.paraCek(500))
print(hesap.get_bakiye())  

