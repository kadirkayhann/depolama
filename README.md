class insan():
    def __init__(self, boy, saç, saç_rengi):
        self.boy = boy
        self.saç = saç
        self.saç_rengi = saç_rengi

    def giris(self):
        metin="""lütfen islem yapmak için sayi girininiz
        1-boy
        2-saç 
        3- saç rengi
        sayi:"""
        veri=int(input(metin))
        if veri == 1 :
           self.boyu_yazdir()
        if veri == 2 :
            self.saç_yazdir()
        if veri == 3 :
            self.saç_rengi_yazdir()
    def boy_sorma (self):
        boy_sor=int(input("lütfen kullanicinin adını giriniz"))
        if boy_sor == "yunus" :
            yunus.boyu_yazdir()
        if boy_sor == "kadir" :
            kadir.boyu_yazdir()

    def saç_sorma(self):
        saç_sor=int(input("lütfen kullanicinin adını giriniz"))
        if saç_sor == "yunus" :
            yunus.saç_yazdir()
        if saç_sor == "kadir" :
            kadir.saç_yazdir
    def saç_rengi_sorma(self):
        saç_rengi_sor=int(input("lütfen kullanicinin adını giriniz"))
        if saç_rengi_sor == "yunus":
            yunus.saç_rengi_yazdir()
        if saç_rengi_sor == "kadir" :
            kadir.saç_rengi_yazdir()

    def boyu_yazdir (self):
        print(self.boy)
    def saç_yazdir (self):
        print(self.saç)
    def saç_rengi_yazdir(self):
        print(self.saç_rengi)
def giriss():
        naber="""lütfen islem yapmak için sayi giriniz
        1-yunus 
        2-kadir
        sayi:"""
        iyi=int(input(naber))
        if iyi == 1 :
            yunus.giris()
        if iyi == 2 :
            kadir.giris()

yunus = insan("220","uzun","mavi")
kadir= insan ("230","kısa","beyaz")



giriss()
