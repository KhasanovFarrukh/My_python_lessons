# 18-DARS. WHILE, RO'YXATLAR VA LUG'ATLAR

"""Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir
qabul qilib, yangi ro'yxatga joylang."""
mahsulotlar = []
while True:
   buyurtma = input('Mahsulot nomini kiriting: ')
   if buyurtma != 'stop':
      mahsulotlar.append(buyurtma)
   else:
      break


"""e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur
yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi)
kiritishni so'rang."""
e_bozor = {
   'anor': 24000,
   'non': 3000,
   'moy': 29000,
   'kartoshka': 5000,
   'qaymoq': 12000
}

while True:
   mahsulot_nomi = input('E-bozor uchun mahsulot nomini kiriting: ')
   if (mahsulot_nomi == 'stop'):
      break
   
   mahsulot_narxi= int(input(f"E-bozor {mahsulot_nomi} mahsulotining narxi: "))
   if (str(mahsulot_narxi) == 'stop'):
      break
   else:
      e_bozor[mahsulot_nomi] = mahsulot_narxi

"""Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir
mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz
mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda
"Bizda bu mahsulot yo'q" degan xabarni kor'sating."""

for mahsulot in mahsulotlar:
   if mahsulot in e_bozor:
      print(f"{mahsulot.title()}ning narxi {e_bozor[mahsulot]} so\'m")
   else:
      print(f"Bizda {mahsulot} mahsuloti yo\'q")
# Output: Bizda anjir mahsuloti yo'q
# Output: Nonning narxi 3000 so'm
# Output: Bizda piyoz mahsuloti yo'q
# Output: Bizda sabzi mahsuloti yo'q
# Output: Qaymoqning narxi 12000 so'm      