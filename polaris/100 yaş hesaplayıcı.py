name = input("Adın nedir? ").title().strip()


print("Hello,", name)


age = int(input(f"Kaç yaşındasın {name}? "))


year = (2125 - age)
print(year, "yılında 100 yaşında olacaksın.")