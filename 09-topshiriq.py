# 9-DARS. FOR TAKRORLASH OPERATORI

"""Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga
takrorlanuvchi xabar yozing. Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta
takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)"""

ismlar = ['Zarina', 'Maftuna', 'Shaxnoza', 'Marjona', 'Jamila']
hisoblagich = 0
for ism in ismlar:
   hisoblagich += 1
   print(f"Salom {ism}")
print(f"Kod {hisoblagich} marta takrorlandi")
# Output: Salom Zarina
# Output: Salom Maftuna
# Output: Salom Shaxnoza
# Output: Salom Marjona
# Output: Salom Jamila
# Output: Kod 5 marta takrorlandi

"""10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring."""
toq_son = list(range(11, 100, 2))

for son in toq_son:
   print(son**3)
# Output: 1331
# Output: 2197
# Output: 3375
# Output: 4913
# Output: ....
# Output: 912673
# Output: 970299

"""Foydalanuvchidan 5 ta eng sevimli kinolarini kiritishni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring."""
kinolar = []

for i in range(1,6):
   kino_nomi = input(f"{i}-sevimli kinoyingizning nomini kiriting: ")
   kinolar.append(kino_nomi)
print(kinolar)
# Output: 1-sevimli kinoyingizning nomini kiriting: who I am
# Output: 2-sevimli kinoyingizning nomini kiriting: bolshoy boss
# Output: 3-sevimli kinoyingizning nomini kiriting: put drakon
# Output: 4-sevimli kinoyingizning nomini kiriting: кибер
# Output: 5-sevimli kinoyingizning nomini kiriting: internet
# Output: ['who I am', 'bolshoy boss', 'put drakon', 'кибер', 'internet']

"""Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang
va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni
konsolga chiqaring."""

suhbat = int(input('Bugun nechta odam bilan suhbat qildingiz?\n>>>'))
suhbatdosh = []

for i in range(1, suhbat+1):
   ism = input(f"{i}-suhbat qilgan odamingiz kim edi: ")
   suhbatdosh.append(ism)
print(suhbatdosh)
# Output: Bugun nechta odam bilan suhbat qildingiz?
# Output: >>>3
# Output: 1-suhbat qilgan odamingiz kim edi: javohir
# Output: 2-suhbat qilgan odamingiz kim edi: iskandar
# Output: 3-suhbat qilgan odamingiz kim edi: jasur
# Output: ['javohir', 'iskandar', 'jasur']