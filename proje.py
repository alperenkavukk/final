a=1
lst=[]
artimaas=4000

class calisan():
    isim=""
    yetenek=""
    mesai=0
    maas=0
    calismagunsayisi=0
    izin=0
    def __init__(self,isim,yetenek,mesai,maas,calismagunsayisi,izin):
        self.isim=isim
        self.yetenek=yetenek
        self.maas=maas
        self.mesai=mesai
        self.calismagunsayisi=calismagunsayisi

    def calis(self):
        self.calismagunsayisi+=1
    def bilgi(self):
        print("ismi: "+self.isim ,"\n","yeteneği: "+self.yetenek,"\n","mesai kaldığı saat :"+str(self.mesai),"\n","aylık maaş :"+str(self.maas),"\n","çalıştığı gün sayısı :"+str(self.calismagunsayisi),"\n","kullandığı izin günü :"+str(self.izin))
bilgii=calisan("alperen","bilgisayar",1,4000,30,0)
bilgi2=calisan("rumk","ingilizce",2,4000,25,5)
isci=bilgii.bilgi()
isci2=bilgi2.bilgi()
print(isci,isci2)


while a==1:

       mesaisaat=int(input("kaç saat mesai yaparsam maasım kaç olur: "))
       izinmaas=int(input("kaç gün izin alırsam maaşım ne olur: "))
       if(mesaisaat==1):
           artimaas+=150
       elif(mesaisaat>1):
           artimaas+=250
       for i in range(izinmaas):
           artimaas-=150
       a=int(input("devam etmek için 1'e basınızz"))
       lst.append(artimaas)

print(lst)





