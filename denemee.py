

class Asker :
    def __init__(self,can,mermi):
        self.can = 100
        self.mermi = 40
        self.düsman_mermi = 30
        self.düsman_can = 100
    def asker(self):

        asker_metin="""lütfen islem yapmak için sayi giriniz
        1-saldır
        2-savun
        sayi:"""
        asker_veri=int(input(asker_metin))
        if asker_veri == 1 :
            naber()
            self.düsman_can -= kac_mermi
            print(selff.cann)
    def düsman(self):
        düşman_metin="""lütfen islem yapmak için sayi giriniz
        1-saldır
        2-savun
        sayi:"""
        düşman_veri=int(input(düşman_metin))
        if düşman_veri == 1  :
            kac_mermi = int(input("kaç mermi harcamak istersiniz"))
            self.can = self.can - kac_mermi

        if düşman_veri == 2  :
            kac_mermi = int(input("kaç mermi harcamak istersiniz"))
            self.can = self.can - kac_mermi

    def giris():

        metin = """lütfen islem yapmak için sayi giriniz
        1-Asker
        2-Düsman    
        veri:"""
        verii = int(input(metin))
        if verii == 1:
            asker()
        if verii == 2:
            düsman()



giris()