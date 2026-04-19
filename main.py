class SozSaralaydi:
    def __init__(self, matn):
        self.matn = matn

    def sozni_chiqar(self):
        sozlar = self.matn.split()
        return sozlar

    def sozlarni_saralash(self):
        sozlar = self.sozni_chiqar()
        sozlar.sort()
        return sozlar

    def sozni_tekshir(self):
        sozlar = self.sozlarni_saralash()
        for soz in sozlar:
            if not soz.isalpha():
                sozlar.remove(soz)
        return sozlar

    def sozni_chiqarish(self):
        sozlar = self.sozni_tekshir()
        return sozlar


class MatnSaralaydi:
    def __init__(self, matn):
        self.matn = matn

    def matnni_saralash(self):
        soz_saralaydi = SozSaralaydi(self.matn)
        sozlar = soz_saralaydi.sozni_chiqarish()
        return sozlar

    def matnni_chiqarish(self):
        sozlar = self.matnni_saralash()
        for soz in sozlar:
            print(soz)


def asosiy():
    matn = "Salom, bugun siz bilan aloqada bo'ladigan python dasturchi. Ushbu dastur siz kiritgan matndagi so'zalrni alifbo tartibida saralaydi"
    matn_saralaydi = MatnSaralaydi(matn)
    matn_saralaydi.matnni_chiqarish()


asosiy()