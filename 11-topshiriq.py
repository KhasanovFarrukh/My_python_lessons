# 11-DARS. BIR NECHTA SHARTLARNI TEKSHIRISH

"""Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa,
"Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring."""
son = int(input('Juft son kiriting: '))
if son>0 and son%2==0:
   print('Rahmat')
else:
   print('Bu juft son emas')
# Output: 5 >>> Bu juft son emas

"""Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm"""
yosh = int(input('Yoshingiz nechida? '))
narx = 0
if yosh <= 4 or yosh >= 60:
   narx = 'bepul'
elif yosh > 4 and yosh < 18:
   narx = 10000
else:
   narx = 20000
print(f"Siz uchun to\'lov narxi: {narx}")

"""Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng
yoki katta/kichikligi haqida xabarni chiqaring."""
bir_son = float(input('Birinchi sonni kiriting: '))
ikki_son = float(input('Ikkinchi sonni kiriting: '))

if bir_son > ikki_son:
   print(f"{bir_son} > {ikki_son}")
elif bir_son < ikki_son:
   print(f"{bir_son} < {ikki_son}")
else:
   print(f"{bir_son} = {ikki_son}")

"""mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi,
savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot
kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va
qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda
yo'q" degan xabarlarni chiqaring."""
mahsulotlar = ['kartoshka', 'piyoz', 'non', 'tuxum', 'guruch', 'sok', 'qand', 'moy', 'tuz', 'karam']
savat = []

for i in range(1,6):
   mahsulot = input(f"{i}-mahsulot nomini kiriting: ")
   savat.append(mahsulot)
   
for mahsulot in savat:
   if mahsulot in mahsulotlar:
      print(f"{mahsulot.title()} mahsuloti do\'konimizda bor")
   else:
      print(f"{mahsulot.title()} mahsuloti do\'konimizda yo\'q")
# Output: Anor mahsuloti do'konimizda yo'q
# Output: Non mahsuloti do'konimizda bor
# Output: Anjir mahsuloti do'konimizda yo'q
# Output: Tuxum mahsuloti do'konimizda bor
# Output: Kolbasa mahsuloti do'konimizda yo'q

"""Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni
so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan
ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar
mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor"
degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni
chiqaring."""
mahsulotlar2 = ['kartoshka', 'piyoz', 'non', 'tuxum', 'guruch', 'sok', 'qand', 'moy', 'tuz', 'karam']
bor_mahsulotlar = []
yoq_mahsulotlar = []

for sanoq in range(1,6):
   mahsulot2 = input(f"{sanoq}-mahsulot nomini kiriting: ")
   if mahsulot2 in mahsulotlar2:
      bor_mahsulotlar.append(mahsulot2)
   else:
      yoq_mahsulotlar.append(mahsulot2)

if len(yoq_mahsulotlar) == 0:
   print(f"Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
   print(f"Quyidagi mahsulotlar do'konimizda yo'q:")
   for yoq_mahsulot in yoq_mahsulotlar:
      print(yoq_mahsulot)
# Output: Quyidagi mahsulotlar do'konimizda yo'q:
# Output: anor
# Output: anjir
# Output: qatiq

"""Foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan
yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan
ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa,
"Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini
chiqaring."""
foydalanuvchilar = ['Farrux', 'Anvar', 'Farhod', 'Ozod', 'Alisher']

login = input('Yangi login tanlang: ')

if login in foydalanuvchilar:
   print(f"{login} logini band, yangi login tanlang")
else:
   print(f"Xush kelibsiz, {login.title()}!")

"""Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni
2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring."""   

kiruvchi_son = int(input('Butun son kiriting: '))

for i in range(2,11):
   if kiruvchi_son%i==0:
      print(f"{kiruvchi_son} soni {i} ga qoldiqsiz bo\'linadi.")
# Output: 66 >>>
# Output: 66 soni 2 ga qoldiqsiz bo'linadi.
# Output: 66 soni 3 ga qoldiqsiz bo'linadi.
# Output: 66 soni 6 ga qoldiqsiz bo'linadi.