# 7-DARS. LIST (RO'YXAT)

"""ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:"""

ismlar = ['Javohir', 'Alisher', 'Iskandar']
print(f"Salom {ismlar[0]}, bugun choyxonaga boramizmi?")
print(f"{ismlar[1]}, choyxonaga boramizmi?")
print(f"{ismlar[2]}, nega choyxonaga bormading?")
# Output: Salom Javohir, bugun choyxonaga boramizmi?
# Output: Alisher, choyxonaga boramizmi?
# Output: Iskandar, nega choyxonaga bormading?

"""sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring."""
sonlar = [251, 96, 0, -62, 12, -32]
sonlar[0] = 152
sonlar[2] = 'nol'
print(sonlar)
# Output: [152, 96, 'nol', -62, 12, -32]

"""t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat
qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning
ismini kiriting. Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib
(.pop()), matn chiqaring."""
t_shaxslar = ['Imom Buxoriy', 'Umar ibn Hattob', 'Holid ibn Valid']
z_shaxslar = ['Bill Gates', 'Ilon Mask', 'Joff Bezos']
print(f"Men tarixiy shaxslardan {t_shaxslar[1]} bilan, zamonaviy shaxslardan esa "
      f"{z_shaxslar[0]} bilan suhbat qilishni istar edim")
# Output: Men tarixiy shaxslardan Umar ibn Hattob bilan, zamonaviy shaxslardan esa Bill Gates bilan suhbat qilishni istar edim

"""friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga
chaqirmoqchi bo'lgan do'stlaringizni kiriting."""
friends = []
friends.append('Ali')
friends.append('Javohir')
friends.append('Iskandar')
friends.append('Chori')
friends.append('Mamatali')
print(f"Mehmonga chaqirilganlar: {friends}")
# Output: Mehmonga chaqirilganlar: ['Ali', 'Javohir', 'Iskandar', 'Chori', 'Mamatali']

"""Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida
o'chirib tashlang."""
friends.remove('Mamatali')
friends.remove('Javohir')
print(f"Kelishi aniq bo\'lgan mehmonlar: {friends}") 
# Output: Kelishi aniq bo'lgan mehmonlar: ['Ali', 'Iskandar', 'Chori']

"""Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing."""
friends.insert(2, 'Ahmad')
friends.insert(0, 'Shavkat')
print(f"Yana chaqirilgan mehmonlar: {friends}")
# Output: Yana chaqirilgan mehmonlar: ['Shavkat', 'Ali', 'Iskandar', 'Ahmad', 'Chori']

"""Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing."""
mehmonlar = []
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(0))
print(f"Kelgan mehmonlar: {mehmonlar}")
# Output: Kelgan mehmonlar: ['Iskandar', 'Shavkat']