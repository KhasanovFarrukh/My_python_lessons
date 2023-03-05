# 15-DARS. LUG'AT ELEMENTLARI BILAN ISHLASH
"""Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi
har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib
konsolga chiqaring."""
lugat = {
   'integer':'butun son',
   'float':'haqiqiy son',
   'string':'matn',
   'if':'agar',
   'else':'aks holda',
   'elif':'aks holda, agar',
   'boolean':'mantiqiy',
   'tuple':'qat\'iy ro\'yhat',
   'list':'ro\'yhat',
   'dict':'lug\'at'
}

for key in sorted(lugat.keys()):
   print(f"{key} so\'zining ma\'nosi - {lugat[key]}")
# Output: boolean so'zining ma'nosi - mantiqiy
# Output: dict so'zining ma'nosi - lug'at
# Output: elif so'zining ma'nosi - aks holda, agar
# Output: else so'zining ma'nosi - aks holda
# Output: float so'zining ma'nosi - haqiqiy son
# Output: if so'zining ma'nosi - agar
# Output: integer so'zining ma'nosi - butun son
# Output: list so'zining ma'nosi - ro'yhat
# Output: string so'zining ma'nosi - matn
# Output: tuple so'zining ma'nosi - qat'iy ro'yhat

"""Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring."""
davlatlar = {
   'rossiya': 'moskva',
   'aqsh': 'vashington',
   'italiya': 'rim',
   'malayziya': 'kuala-lumpur',
   'o\'zbekiston': 'toshkent',
   'singapur': 'sungapur',
   'tojikiston': 'dushanbe'
}

print('Dunyo davlatlari:')
for davlat in sorted(davlatlar.keys()):
   if davlat == 'aqsh':
      print(davlat.upper())
   else:
      print(davlat.title())
print('***********************')
print('Dunyo poytaxtlari:')
for poytaxt in sorted(davlatlar.values()):
   print(poytaxt.title())
# Output: Dunyo davlatlari:
# Output: AQSH
# Output: Italiya
# Output: Malayziya
# Output: O'Zbekiston
# Output: Rossiya
# Output: Singapur
# Output: Tojikiston
# Output: ***********************
# Output: Dunyo poytaxtlari:
# Output: Dushanbe
# Output: Kuala-Lumpur
# Output: Moskva
# Output: Rim
# Output: Sungapur
# Output: Toshkent
# Output: Vashington

"""Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini
konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday
ma'lumot yo'q" degan xabarni chiqaring."""

davlat_nomi = input('Davlat nomini kiriting: ')
if davlat_nomi not in davlatlar.keys():
   print('Bizda bunday ma\'lumot yo\'q')
else:
   if davlat_nomi == 'aqsh':
      print(f"{davlat_nomi.upper()}ning poytaxti {davlatlar[davlat_nomi].title()} shahri")
   else:
      print(f"{davlat_nomi.title()}ning poytaxti {davlatlar[davlat_nomi].title()} shahri")
# Output: Malayziyaning poytaxti Kuala-Lumpur shahri

"""Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni
menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda
"bizda bunday taom yo'q" degan xabarni chiqaring."""
taomlar = {
   'osh': 18000,
   'manti': 6000,
   'shashlik': 14000,
   'somsa': 12000,
   'tandir kabob': 180000,
   'cho\'poncha': 150000,
   'mastava': 17000,
   'gamburger': 22000,
   'sho\'rva': 15000,
   'pizza': 28000
}
buyurtmalar = []
for i in range(1,4):
   taom = input(f"{i}-taom nomini kiriting: ")
   buyurtmalar.append(taom)

for buyurtma in buyurtmalar:
   if buyurtma in taomlar:
      print(f"{buyurtma.title()} narxi {taomlar[buyurtma]} so\'m")
   else:
      print(f"Kechirasiz, bizda {buyurtma} yo\'q")
# Output: Osh narxi 18000 so'm
# Output: Manti narxi 6000 so'm
# Output: Kechirasiz, bizda xonim yo'q
