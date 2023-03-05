# 6-DARS. SONLAR

"""Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur"""
son = int(input('Sonni kiriting: '))
print(f"{son} ning kvadrati {son**2} ga teng")
print(f"{son} ning kubi {son**3} ga teng")
# Output: 45 ning kvadrati 2025 ga teng
# Output: 45 ning kubi 91125 ga teng

"""Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur"""
yosh = int(input('Yoshingiz nechida? '))
t_yil = 2023 - yosh
print(f"Siz {t_yil} da tug\'ilgansiz")
# Output: Siz 1993 da tug'ilgansiz

"""Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur"""
birinchi_son = float(input('Birinchi sonni kiriting: '))
ikkinchi_son = float(input('Ikkinchi sonni kiriting: '))

yigindi = birinchi_son + ikkinchi_son
ayirma = birinchi_son - ikkinchi_son
kopaytma = birinchi_son * ikkinchi_son
bolinma = birinchi_son / ikkinchi_son
print(f"{birinchi_son} + {ikkinchi_son} = {yigindi}")
print(f"{birinchi_son} - {ikkinchi_son} = {ayirma}")
print(f"{birinchi_son} * {ikkinchi_son} = {kopaytma}")
print(f"{birinchi_son} / {ikkinchi_son} = {bolinma}")
# Output: 45.0 + 12.0 = 57.0
# Output: 45.0 - 12.0 = 33.0
# Output: 45.0 * 12.0 = 540.0
# Output: 45.0 / 12.0 = 3.75