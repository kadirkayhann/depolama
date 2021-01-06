import random

class Asker:

    def __init__(self, isim, can):
        self.isim = isim
        self.can = can
        self.sarjor = 30

    def saldir(self):
        self.mermi_gucu = random.randint(5, 10)
        harcanan_mermi = random.randint(1, 6)
        self.sarjor = self.sarjor - harcanan_mermi
        return harcanan_mermi * self.mermi_gucu


class Dusman:

    def __init__(self, isim, can):
        self.isim = isim
        self.can = can
        self.sarjor = 30

    def saldir(self):
        self.mermi_gucu = random.randint(5, 10)
        harcanan_mermi = random.randint(1, 6)
        self.sarjor = self.sarjor - harcanan_mermi
        return harcanan_mermi * self.mermi_gucu

    def savun(self, gelen_hasar):
        savunulan_hasar = random.randint(0, gelen_hasar)        
        self.can = self.can - (gelen_hasar - savunulan_hasar)
        return self.can

asker = Asker('isim', 100)
dusman = Dusman('isim', 100)

a = asker.saldir()
print(a)
print(dusman.savun(a))