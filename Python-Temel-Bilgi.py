ad="selcuk"

print(len(ad))#karekterin sayısını gösterir.
print(ad*5)#5kere yazar.

print(ad.upper())#Hepsini büyük yazar.
print(ad.lower())#hepsini küçük yazar.

print(5**2)#5 üzeri 2
print(16 // 5)#bölümü sadece tam kısmı yazar.
print(abs(-12))#Mutlak değer yapar.
print(round(22/7))#sonucu yuvarlar yapar.
print(round(3.4564,3))#3 basamak yuvarlar.

print(ad.islower())#tamamen küçükse true.
print(ad.isupper())#tamamen büyükse true.
print(ad.capitalize())#Baş harfini büyültür.
print(ad.startswith("se"))#Neyle başladığını kontrol ediyoruz.
print(ad.endswith("cuk"))#Neyle bittiğini kontrol eder.
print(ad.title())#Her kelimenin baş harfini büyük yazar
print(ad.split())#Dizi şekline getirir.


print("merhaba {}".format(ad))#{içine adı yazar}

print(f"Merhaba {ad}")#{içine adı yazar}

print(ad.replace("s","k"))#s harfi yerine k harfi koyar.

print(ad.strip())#köşelerdeki boşlukları kırpar.strip(içine kırpılacak bişey koyabilirsin)

#print(dir(ad)) uygulanabilen metodları görürüz.

print(ad[0:3])#sol dahil sağ dahil deil.

print(type(ad))#türünü yazar.

print("selcuk","coskun",sep="-")#araya koyar.

"""
bu şekildede satirli yorum satiri yapilir.

"""
############################################################################################
ad=input("adinizi girin=")#kullanıcıdan veri almak.herzaman string türündedir.
int(ad)#karakteri sayi yapar.str,float başına yazılır.
del ad[0] #silme
###  []=list     ()=tuple    {}=dictinory    True,False=Boolen
############################################################################################
#LİSTELER
renkler=["Sari","Yeşil","Mor","Mavi"]
print(renkler[1])##Yeşili yazar
print(renkler[2:])##Mor ve Mavi yazar.

renkler.append("Gri")#Listemin sonuna ekledim.

renkler.insert(0,"Gri")# 0.yere ekledim.

renkler.remove("Sari")#Sariyi sildi.

renkler.pop(0)#0.elamanı siler

renkler.index("Sari")#Kaçıncı indekte

print("Sari" in renkler)#Sari varmi yokmu ona bakar.

renkler2=["Turuncu","Siyah","Beyaz"]
renkler.extend(renkler2)#sonuna ekledi.

renkler.pop()#son elamanı siler.(içine yerini yazabilirsin)
silinen =renkler.pop()#silinen elamanı gösterir.

renkler.reverse()#tersine çevirir.

renkler.sort()#Alfabetik olarak sıralar,Sayı varsa büyükten küçüğe.

renkler.count("Sari")#Kaç kere olduğunu söyler.

sayilar=[1,2,3,4,5,6,7,8]

print(min(sayilar))#en küçük sayiyi yazar.renklerde en baştakini yazar
print(max(sayilar))#en büyük sayiyi yazar.renkleri yaparsan en ilerdekini yazar

print(sum(sayilar))#sayilari toplar.

print("Sari" in renkler)#İçinde varmı ona bakar.

##########################################################################################
#TUPLE(DEMET)
renk=("Sari","Yeşil","Mavi","Mor")
#Elamanları değiştirilemez.
##########################################################################################
#Küme(SET)
renkler={"Sari","Yeşil","Mavi","Mor"}
#Sırasız bir veri yapısıdır.Her elaman 1 kere olur.
renkler.add("Pembe")#pembe eklendi
renkler.remove("Sari")#Sariyi siler.
renkler.discard("Sari")#Sariyi siler.
renkler2={"Sari","Mavi","Kirmizi"}
print(renkler.intersection(renkler2))#keşisimini verir.
print(renkler.union(renkler2))#Birleşimini yazar.
print(renkler.difference(renkler2))#renklerde olup renkler2de olmayan şeyler.

print("Sari" in renkler)#renkler kümesinde Sari varmi ona bakar.

###################################################################
#SÖZLÜK
kişi={"isim" : "selcuk", "no" : 123, "cinsiyet":"erkek"}

print(kişi["isim"])#ismini yazar.

kişi["isim"]="Ali"#ismini değiştirir.

kişi.update({"isim":"Ahmet","no":132})#çoklu değişiklik.

kişi["soyad"]="coskun"#ekleme yaptık

del kişi["isim"]#ismini sildik.

####################################################################
a=5
b=3
if a==b or b==a:
    print("Eşit")
else:
    print("Eşit deil")

#or=veya
#and=ve
#in=kontrol eder.
renkler=["Sari","Yeşil","Mavi","Mor"]
a=input("Renk gir")
if a in renkler:
    print("İçinde var")
else:
    print("İçinde yok")
######################################################################
for i in range(1,10):
 print(i)#1,2,3,4,5,6,7,8,9 yazar.

i=1

while i<10:
   print(i)#1,2,3,4,5,6,7,8,9 yazar.
   i=i+1

######################################################################
#Fonksiyonlar
def asal(x):
   for i in range(2,x//2):
      if x % i ==0:
         print("Asal değil")
         break
      else:
         print("Asal")

##########################################################################
#Modüller
import math
print(math.factorial(5))#5 sayisinin faktoriyelini aldi.

math.fabs(-5)#Mutlak değer alir.
math.sqrt(9)#Karekök içine alir.

#Rastgele 10 tane sayi yaziyor
import random

for i in range(1,10):
    print(random.random())
#sizin belirledğiniz aralikta rastgele sayi yazar.
import random

for i in range(1,10):
    print(random.uniform(10,20))#10-20 araliğinda rastgele sayi yazacak.

##########################################################################
import os#İşletim sistemiyle ilgili bir modül.

print(os.getcwd())#Hangi klasördeyiz onun tam konumunu gösterir.

os.chdir("c:\Users\User\Desktop")#Klasör değiştirme
print(os.listdir())#Klasörün içeriğini verir.
os.mkdir("Deneme_Klasörü")#Klasör oluşturur.
os.rmdir("Deneme_Klasörü")#Klasör silinir.
###########################################################################
#DOSYA İŞLEMLERİ#
a =open("selcuk.txt","r")#Dosyayı açtık
print(a.read())#Okuruz
a.close()#Dosyayı kapattık
##-----------------

with open("C:/Users/User/Desktop\python kodları/kali temel kodlar..txt","r") as dosya:#r read okumak.
   print(dosya.read())#dosyayı okuruz

with open("C:/Users/User/Desktop\python kodları/deneme.txt","w") as dosya:#w write yazmak.
   dosya.write("Selçuk")#Dosyaya Selçuk yazar

