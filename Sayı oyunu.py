print("sayi oyununa hos geldiniz")

number = 32 

playernumbers = int(input("o ile 50 arasinda bir sayi tahmin ediniz"))

change = 3 

while True:
    if change != 0:
        if playernumbers > number:
          change -= 1 
          print(change, "hakkınız kaldı")
          playernumbers = int("daha küçük bir sayi giriniz.")
        elif playernumbers < number:
              change -= 1
              print(change, "hakkınız kaldi")
              playernumbers = int(input("daha büyük bir sayı giriniz"))

        if playernumbers == number:
                  print("tebrikler oyunu kazandınız")
                  break


    if change == 0:
        print("üzgünüm oyunu kaybettiniz :(")
        break