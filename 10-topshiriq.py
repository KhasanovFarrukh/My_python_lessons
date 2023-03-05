# 10-DARS. IF-ELSE

"""Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat
elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni
katta qiling."""

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for car in cars:
   if car == 'gm':
      print(car.upper())
   else:
      print(car.title())
# Output: Toyota
# Output: Mazda
# Output: Hyundai
# Output: GM
# Output: Kia

"""Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring."""
for car in cars:
   if car != 'gm':
      print(car.title())
   else:
      print(car.upper())
# Output: Toyota
# Output: Mazda
# Output: Hyundai
# Output: GM
# Output: Kia

"""Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda,
"Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring."""
ism = input('Loginingizni kiriting: ')
if ism.lower() == 'admin':
   print(f"Xush kelibsiz, {ism.title()}. Foydalanuvchilar ro\'yxatini ko\'rasizmi?")
else:
   print(f"Xush kelibsiz, {ism.title()}!")
# Output: Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?
# Output: Xush kelibsiz, Farrux! 

"""Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa,
"Sonlar teng" ekan degan yozuvni konsolga chiqaring."""

bir_son = int(input('Birinchi sonni kiriting: '))
ikki_son = int(input('Ikkinchi sonni kiriting: '))

if bir_son == ikki_son:
   print('Sonlar teng')
# Output: Sonlar teng

"""Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga
"Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring."""

istalgan_son = int(input('Sonni kiriting: '))
if istalgan_son < 0:
   print('Manfiy son')
else:
   print('Musbat son')
# Output: Manfiy son

"""Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini
hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni
chiqaring."""
musbat_son = int(input('Musbat sonni kiriting: '))
if musbat_son > 0:
   print(f"{musbat_son} sonining ildizi", musbat_son**(1/2))
else:
   print('Musbat son kiriting')
# Output: 25 sonining ildizi 5.0