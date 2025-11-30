score = int(input("Sınav Notu(0-100): "))

if 0 <= score <= 50:
    print("Kaldı")

elif score <= 100:
    print("Geçti")



else:
   score2 = int(input("Lütfen geçerli bir sayı girin: "))


   if 0 <= score2 <= 50:
       print("Kaldı")

   elif score2 <= 100:
       print("Geçti")

   else:
       print(">:(")