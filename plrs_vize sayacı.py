from datetime import datetime

def main():
    exam_date_str = input("sınav tarih ve saatinizi girin (gün-ay-yıl saat.dakika): ")


    try:

         exam_date = datetime.strptime(exam_date_str, "%d-%m-%Y %H.%M")


         current_date = datetime.now()


         time_diff = exam_date - current_date


         days_left = time_diff.days
         hours_left = time_diff.seconds // 3600
         minutes_left = (time_diff.seconds % 3600) // 60

         if days_left >=0:
              print(f"sınavınıza {days_left} gün, {hours_left} saat, {minutes_left} dakika kaldı.")
        
         else:
              print("Sınavınız geçti!")
    except ValueError:
         print("Geçersiz tarih formatı. Lütfen 'gün-ay-yıl saat.dakika' formatında giriniz.")
       

main()