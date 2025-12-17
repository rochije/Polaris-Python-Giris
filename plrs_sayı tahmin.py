import random 
guess = random.randint(1,100)

x = int(input("tuttuğum sayı ne? "))

while True:
    if x < guess:
       print("yukarı çık")
      
    elif x > guess:
        print("aşağı in")
    
    else:
        print("Doğru! Tebrikler ")
        break

    x = int(input("tekrar deneyin: "))
