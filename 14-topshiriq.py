# 14-DARS. LUG'AT BILAN TANISHUV

"""Otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida
kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring =>
Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan."""
otam = {
   'ismi':'Umar',
   't_yili': 1969,
   't_viloyati': 'Farg\'ona',
   'tel_raqami':'93-644-07-07'
}
print(f"Otamning ismi {otam['ismi']}, {otam['t_yili']}-yilda, {otam['t_viloyati']} viloyatida tug\'ilgan.")
# Output: Otamning ismi Umar, 1969-yilda, Farg'ona viloyatida tug'ilgan.


"""Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom
juftligi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring =>
Alining sevimli taomi osh."""
taom = {
   'alisher': 'manti',
   'iskandar': 'somsa',
   'ahmad': 'kabob',
   'shavkat': 'cho\'poncha',
   'jasur': 'osh'
}
print(f"Alisherning sevimli taomi {taom['alisher']}")
print(f"Ahmadning sevimli taomi {taom['ahmad']}")
print(f"Jasurning sevimli taomi {taom['jasur']}")
# Output: Alisherning sevimli taomi manti
# Output: Ahmadning sevimli taomi kabob
# Output: Jasurning sevimli taomi osh


"""Python izohli lug'ati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani)
kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha
tarjimasini yozing."""

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

"""Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi
lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas"
degan xabarni chiqaring."""
soz = input('So\'zni kiriting: ')
if soz in lugat.keys():
   print(f"{soz}i so\'zi {lugat[soz]} deb tarjima qilinadi")
else:
   print('Bunday so\'z mavjud emas')
# Output: dict >>> lug'at