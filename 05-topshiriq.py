# 5-DARS. STRING (MATN)

"""Quyidagi o'zgaruvchilarni yarating: 
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati"""
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor" 
viloyat = "Samarqand"
print(kocha, 'ko\'chasi', mahalla, 'mahallasi', tuman, 'tumani', viloyat, 'viloyati')
# Output: Bog'bon ko'chasi Sog'bon mahallasi Bodomzor tumani Samarqand viloyati

"""Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang."""
kocha = input('Ko\'cha nomini kiriting: ')
mahalla = input('Mahalla nomini kiriting: ')
tuman = input('Tuman nomini kiriting: ')
viloyat = input('Viloyat nomini kiriting: ')
print(kocha, 'ko\'chasi', mahalla, 'mahallasi', tuman, 'tumani', viloyat, 'viloyati')
# Output: Ahmad Yassaviy ko'chasi Do'stlik mahallasi Qiziriq tumani Sirdaryo viloyati

"""Yuqoridagi matnni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang."""
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor" 
viloyat = "Samarqand"
yangi_manzil = f"{kocha} ko\'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati"
print(yangi_manzil)
# Output: Ahmad Yassaviy ko'chasi Do'stlik mahallasi Qiziriq tumani Sirdaryo viloyati

"""manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring."""
print(yangi_manzil.upper())
# Output: BOG'BON KO'CHASI SOG'BON MAHALLASI BODOMZOR TUMANI SAMARQAND VILOYATI