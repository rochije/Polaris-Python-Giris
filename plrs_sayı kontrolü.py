def main():
    x = get_int("Sayıyı girin: ")
    print(f"Girdiğiniz {x} değeri bir sayıdır.")


def get_int(prompt):
    while True:
       try:
            x = int(input(prompt))

       except ValueError:
            print("Lütfen geçerli bir sayı giriniz. ")
       break
main()