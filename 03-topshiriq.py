# 3-DARS. PRINT(), SINTAKSIS VA ARIFMETIK AMALLAR

"""Quyidagi matnni aynan shunday ko'rinishda konsolda chiqaring:
"Nexia", "Tico", 'Damas' ko'rganlar qilar havas"""
print(f"\"Nexia\", \"Tico\", 'Damas' ko\'rganlar qilar havas")
# Output: "Nexia", "Tico", 'Damas' ko'rganlar qilar havas

"""5 ning 4-darajasini toping"""
print('5 ning 4-darajasi', 5**4)
# Output: 5 ning 4-darajasi 625

"""22 ni 4 ga bo'lganda qancha qoldiq qoladi?"""
print(f"22 ni 4 ga bo\'lganda {22 % 4} qoldiq qoladi")
# Output: 22 ni 4 ga bo'lganda 2 qoldiq qoladi

"""Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping"""
tomon = 125
print(f"Tomonlari {tomon} ga teng bo\'gan kvadratning yuzi: {tomon**2} va perimetri {tomon*4} ga teng")
# Output: Tomonlari 125 ga teng bo'gan kvadratning yuzi: 15625 va perimetri 500 ga teng

"""Diametri 12 ga teng bo'lgan doiraning yuzini toping  (pi=3.14 deb oling)"""
diametr = 12
PI = 3.14
doira_yuzi = PI*((diametr/2)**2)
print(f"Diametri {diametr} ga teng bo\'gan doiraning yuzi {doira_yuzi} ga teng")
# Output: Diametri 12 ga teng bo'gan doiraning yuzi 113.04 ga teng

"""Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)"""
katet_1 = 6
katet_2 = 7
gipotenuza = katet_1**2 + katet_2 ** 2 # Pifagor teoremasi: c^2=a^2+b^2
print(f"Katetlari {katet_1} va {katet_2} bo\'lgan to\'g\'ri burchakli uchburchakning giponenizasi {gipotenuza**(1/2)} ga teng")
# Output: Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning giponenizasi 9.219544457292887 ga teng