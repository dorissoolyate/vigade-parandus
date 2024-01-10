
# from random import *
# a=randint(-100,200)
# #esli delica bez ostatka, 4etnoe 4islo, ==0 tipo bez ostatka
# #
# if a%2==0:
#     print("juhuslik arv on",a)
#     print(a,"-paaris arv")

# if a>0:
#     print(a,"suurem kui 0")
# else:
#     print (a,"vaiksem kui 0 voi vordne 0-ga")

# #<0,>100 ei sobi, 0-59-"2",60-75-"3", 76-90-"4", 91-100-"5"
# if a<0 or a>100:
#     print("viga tulemusega")
# elif a>=0 and a<60:
#     print("hinne 2")
# elif a>=60 and a<=75:
#     print("hinne 3")
# elif a>=76 and a<91:
#     print("hinne 4")
# else:
#     print("hinna 5")
# from random import*

#zadanie1
# nimi=input("kak zovut?") #upper()-"JUKU", lower()-"juku"
# if nimi=="juku":
#     print("poshli v kino")
# vanus=int(input("kirjuta vanus:"))
# if vanus<0 or vanus>100:
#     print("viga, kirjuta vanus0-100")
# elif vanus<6:
#     print("tasuta pilet")
# elif 6 <= vanus <= 14:
#     print("lastepilet")
# elif 15 <= vanus <= 65:
#     print("taispilet")
# else:
#     print("sooduspilet")

#zadanie 2
# nimi1=input("kak zovut?")
# nimi2=input("kak zovut?")
# if nimi1=="eva"and nimi2=="olga" or nimi1=="olga" and nimi2=="eva":
#     print("sosedi")
# else:
#     print("nea")
    

#zadanie 3
# pikkus=float(input("skolko metrov dlina"))
# laius=float(input("skolko metrov laius"))
# pindala=pikkus*laius
# print(f"pindala on {pindala} kv.metrov")
# remont=input("remont ho4esh? da/net")
# if remont=="da":
#     cena_kv_metra=float(input("skolko cena za kv metr"))
#     summa=pindala*cena_kv_metra
#     print(f"cena remonta {summa} eur")
# else:
#     print("ne ho4et remont")

#zadanie 4
# alghind=float(input("skolko alghind"))
# if alghind > 700:
#     prots_skidki = 30
#     cena_skidki=alghind-(alghind*prots_skidki/100)
#     print(f"so skinkoj 30% stoit {cena_skidki} eur ")
# else:
#     print("dlja skidki cena dolzna byt bolee 700")

#zadanie 5
# temp=float(input("skolko temp"))
# if temp>18:
#     print("temp bolshe 18")
# else:
#     print("temp 18 ili menshe")
    
#zadanie 6
# rost=float(input("kakoj rost"))
# kraj_korotkogo=160
# kraj_dlinnogo=180
# if rost<kraj_korotkogo:
#     print("karlik")
# elif kraj_korotkogo<=rost<=kraj_dlinnogo:
#     print("norm")
# else:
#     print("dlinnyj")
                        
    