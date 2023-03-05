# 16-DARS. NESTING
"""Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi
ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har
bir shaxs haqidagi ma'lumotni konsolga chiqaring."""
jobs = {
   'ism':'steve',
   'familiya':'job',
   'kompaniya':'apple',
   'lavozim':'vafot etgan',
   'mahsulot': ['apple', 'iphone', 'macbook', 'air pots']
}

gates = {
   'ism':'bill',
   'familiya':'gates',
   'kompaniya':'microsoft',
   'lavozim':'boshqaruv kengashi a\'zosi',
   'mahsulot': ['windows', 'office', 'nokia', 'bing', 'github']
}

musk = {
   'ism':'elon',
   'familiya':'mask',
   'kompaniya':'tesla',
   'lavozim':'kompaniya raisi',
   'mahsulot': ['tesla', 'twitter', 'skylink']
}

bezos = {
   'ism':'jeff',
   'familiya':'bezos',
   'kompaniya':'amazon',
   'lavozim':'kompaniya direktori',
   'mahsulot': ['amazon', 'orange', 'AWS']
}

tanlanganlar = [jobs, gates, musk, bezos]

for tanlangan in tanlanganlar:
   print(f"{tanlangan['ism'].title()} {tanlangan['familiya'].title()}",
         f"\"{tanlangan['kompaniya'].title()}\" kompaniyasi asoschisi.",
         f"Hozirgi kunda u {tanlangan['lavozim']}")
# Output: Steve Job "Apple" kompaniyasi asoschisi. Hozirgi kunda u vafot etgan
# Output: Bill Gates "Microsoft" kompaniyasi asoschisi. Hozirgi kunda u boshqaruv kengashi a'zosi
# Output: Elon Mask "Tesla" kompaniyasi asoschisi. Hozirgi kunda u kompaniya raisi
# Output: Jeff Bezos "Amazon" kompaniyasi asoschisi. Hozirgi kunda u kompaniya direktori


"""Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring."""
for tanlangan in tanlanganlar:
   print(f"{tanlangan['ism'].title()} {tanlangan['familiya'].title()} tomonidan yaratilgan mahsulotlar")
   for mahsulot in tanlangan['mahsulot']:
      print(mahsulot.upper())
# Output: Steve Job tomonidan yaratilgan mahsulotlar
# Output: APPLE
# Output: IPHONE
# Output: MACBOOK
# Output: AIR POTS
# Output: Bill Gates tomonidan yaratilgan mahsulotlar
# Output: WINDOWS
# Output: OFFICE
# Output: NOKIA
# Output: BING
# Output: GITHUB
# Output: Elon Mask tomonidan yaratilgan mahsulotlar
# Output: TESLA
# Output: TWITTER
# Output: SKYLINK
# Output: Jeff Bezos tomonidan yaratilgan mahsulotlar
# Output: AMAZON
# Output: ORANGE
# Output: AWS

"""Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga
saqlang.  Natijani konsolga chiqaring."""

dostlar = {
   'bekzod': [],
   'iskandr': [],
   'jasur': []
}

for person in dostlar.keys():
   print(f"{person.title()} sevimli filmlaringizni kiriting!")
   for i in range(1,4):
      kino = input(f"{i}-sevimli kinoyingizning nomini kiriting: ")
      dostlar[person].append(kino)

for person in dostlar.keys():
   print(f"{person.title()}ning sevimli filmlari")
   for film in dostlar[person]:
      print(f"- {film.title()}")
# Output: Bekzodning sevimli filmlari
# Output: - Terminator
# Output: - Rambo
# Output: - Titanic
# Output: Iskandrning sevimli filmlari
# Output: - Tenet
# Output: - Inception
# Output: - Interstellar
# Output: Jasurning sevimli filmlari
# Output: - Abdullajon
# Output: - Bomba
# Output: - Shaytanat

"""Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida
ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga
chiqaring."""
davlatlar = {
   'o\'zbekiston': {
      'poytaxt': 'toshkent',
      'hudud': 448978,
      'aholi': 36000000,
      'pul': 'so\'m'
   },
   'rossiya': {
      'poytaxt': 'moskva',
      'hudud': 17098246,
      'aholi': 144000000,
      'pul': 'rubl'
   },
   'aqsh': {
      'poytaxt': 'vashington',
      'hudud': 9631418,
      'aholi': 327000000,
      'pul': 'dollar'
   },
   'malayziya': {
      'poytaxt': 'kuala-lumpur',
      'hudud': 329750,
      'aholi': 25000000,
      'pul': 'rinngit'
   }
}
for davlat in davlatlar.keys():
   print(f"{davlat.title()}ning poytaxti {davlatlar[davlat]['poytaxt'].title()}\n",
         f"Hududi: {davlatlar[davlat]['hudud']}\n",
         f"Aholisi: {davlatlar[davlat]['aholi']}\n",
         f"Pul birligi: {davlatlar[davlat]['pul']}")