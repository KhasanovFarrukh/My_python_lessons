# 19-DARS. FUNKSIYA
"""Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya
yozing."""
ism = input('Ismingizni kiriting: ')
yosh = int(input('Yoshingizni kiriting: '))

def tYil(yosh):
   return 2023 - yosh
print(f"{ism.title()}bek, siz {tYil(yosh)}-yilda tug\'ilgansiz")
# Output: Farruxbek, siz 1992-yilda tug'ilgansiz


"""Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya
yozing."""
son = float(input('Son kiriting: '))
def qiymat(son):
   print(f"{son} sonining kvadrati {son**2}, kubi {son**3} ga teng")
qiymat(son)
# Output: 2.0 sonining kvadrati 4.0, kubi 8.0 ga teng


"""Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya
yozing."""
toq_juft = int(input('JUFT/TOQ - sonni kiriting: '))
def toqJuft(toq_juft):
   if toq_juft%2==0:
      return f"{toq_juft} soni juft son"
   else:
      return f"{toq_juft} soni toq son"
print(toqJuft(toq_juft))
# Output: 156547 soni toq son


"""Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya
yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring."""

son_bir = float(input('Birinchi sonni kiriting: '))
son_ikki = float(input('Ikkinchi sonni kiriting: '))

def maximum(mini, maxi):
   if maxi > mini:
      return f"Katta son {maxi}"
   elif mini > maxi:
      return f"Katta son {mini}"
   else:
      return 'Sonlar teng'
print(maximum(son_bir, son_ikki))


"""Foydalanuvchidan x va y sonlarini olib, x^yni konsolga chiqaruvchi funksiya yozing."""
x = int(input('X sonini kiriting: '))
y = int(input('Y sonini kiriting: '))

def daraja(x, y=2):
   return x**y
print(f"{x} sonining {y}-darajasi {daraja(x,y)} ga teng")
# Output: 2 sonining 4-darajasi 16 ga teng


"""Yuqoridagi funksiyada y uchun 2 standart qiymatini bering."""
def darajaY(x, y=2):
   return x**y
print(f"{x} sonining {y}-darajasi {daraja(x,y)} ga teng")
# Output: 7 sonining 2-darajasi 49 ga teng


"""Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz
bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring."""

bolinuvchi = int(input('Bo\'linuvchi sonni kiriting: '))
def boluvchi(bolinuvchi):
   for i in range(2,11):
      if bolinuvchi%i==0:
         print(f"{bolinuvchi} soni {i} soniga qoldiqsiz bo\'linadi")
boluvchi(bolinuvchi)
# Output: 99 soni 3 soniga qoldiqsiz bo'linadi
# Output: 99 soni 9 soniga qoldiqsiz bo'linadi