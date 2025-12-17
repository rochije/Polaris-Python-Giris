def main():
    x = get_int("Sayıyı girin: ")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            print(f"Girdiğiniz {x} değeri bir sayıdır.")
             
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")


main()
