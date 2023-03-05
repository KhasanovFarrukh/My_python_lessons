# 17-DARS. WHILE SIKLI
"""Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop
so'zini yozishi bilan dasturni to'xtating."""
bayroq = True
kitoblar = []
while bayroq:
   kitob = input('Yaxshi ko\'rgan kitobingiz nomini kiriting: ')
   kitoblar.append(kitob)
   if kitob == 'stop':
      bayroq = False
print('Sizning yaxshi ko\'rgan kitoblaringiz ro\'yhati:', kitoblar)

"""Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm,
7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while
sikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring)"""

flag = True

while flag:
   yosh = (input('Yoshingiz kiriting: '))
   if (yosh == 'quit') or (yosh == 'exit'):
      print('Dasturdan chiqamiz')
      break

   yosh = int(yosh)
   if yosh < 7:
      print('Chipta narxi 2000 so\'m')
   elif yosh >= 7 and yosh < 18:
      print('Chipta narxi 3000 so\'m')
   elif yosh >= 18 and yosh <= 65:
      print('Chipta narxi 10000 so\'m')
   elif yosh > 65 and yosh <= 120:
      print('Chipta bepul')
   elif yosh > 120:
      print('Bu yoshga kirgan odam muzeyga borolmasa kerak-aaa???')
