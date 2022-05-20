"""
Kullanıcıdan 1.vize ve 2.vize  final not girilmesi istensin not aralığı 0 ile 100 arasında olmalıdır.
## vize ve finalin ortalaması alınsın.
## 0-44 : Kaldınız
## 45-69: Geçtiniz
## 70-84: İyi
## 85-100: Pekiyi
"""

# vize1 = int(input("1. vize notunuzu giriniz: "))
# vize2 = int(input("2. vize notunuzu giriniz: "))
# final = int(input("Final notunuzu giriniz: "))
#
# if 0 <= vize1 and vize1 <= 100:
#     pass
# else:
#     print("1. vize hatalı giriş." )
#
# if 0 <= vize2 and vize2 <= 100:
#     pass
# else:
#     print("2. vize hatalı giriş.")
#
# if 0 <= final and final <= 100:
#     pass
# else:
#     print("Final hatalı giriş." )
#
# ortalama = (((vize1+vize2)/2)*0.4)+(final*0.6)
# print("Ortalamanız:", ortalama)
#
# if ortalama > 0 and ortalama < 45:
#     print("KALDINIZ")
# elif ortalama > 44 and ortalama < 70:
#     print("GEÇTİNİZ")
# elif ortalama > 69 and ortalama < 85:
#     print("İYİ")
# elif ortalama > 84 and ortalama < 101:
#
#     print("PEKİYİ")
# else:
#     print("Hata")

"""
# ÖDEV: Kullanıcı Gİriş Paneli Tasarlayınız.

    Kullanıcıadı/Email ve şifre ile giriş sağlanacak
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz? 
                Hayır ise PEKİ!!! 
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması 
"""

# username = "can"
# e_mail = "ozelcan@gmail.com"
# password= "123"
#
# kulinaci_adi = e_posta = input("Kulanıcı adı veya E-posta  giriniz: ")
# sifre = input("Şifrenizi giriniz: ")
#
#
# if (kulinaci_adi == username  ) or (e_posta == e_mail) and  (sifre == password ):
#     print("Giriş başarılı.")
#
# elif (kulinaci_adi == username ) or (e_posta == e_mail)  and (sifre != password):
#     print("Şifre hatalı tekrar deneyin.")
#     sifre = input("Şifrenizi giriniz: ")
#     if sifre == "123":
#      print("Giriş başarılı")
#     else:
#      print("Şifre hatalı.")
#
# elif (kulinaci_adi != username) or (e_posta != e_mail)  and (sifre != password) :
#     print("Kulanıcı bulunamdı, kayıt olmak ister misiniz?")
#     cevap = (input("Cevabınız girin (EVET VEYA HAYIR):"))
#     cevap = cevap.lower()
#     if cevap == ("evet"):
#      print("-Kayıt ekranına yönlendirliyorsunuz-")
#      kulanıcıAdi = input("Kulanıcı adınızı giriniz:")
#      isim = input("Adınız giriniz: ")
#      soyad = input("Soyadınız giriniz: ")
#      eposta = input("E-postanızı giriniz: ")
#      sifre1 = input("Şifrenizi giriniz: ")
#      sifre2 = input("Şifrenizi tekrar giriniz: ")
#      if sifre1 == sifre2:
#          print("Kaydınız alınmıştır.")
#      else:
#          print("Şifreler uyuşmuyor")
#     else:
#      print("Peki")
# else:
#     print("Hata")

"""
# ÖDEV: Kullanıcıdan isim,yaş,maaşve çocuk sayısı alalım

    Eğer kullanıcının yaşı 45'in altındaysa;
        çocuk sayısına bakılacak ve çocuk sayısı 3^ten az ise çocuk başına 250₺, değilse çocuk başına 200₺ maaşa eklenecek
    Eğer kullanıcının yaşı 45 ve üzerinde ise:
        çocuk başına para verilmeyecek direk 500₺ maaşa eklenecek.
    Ekrana "Nesrin Yılmaz Maaşınız: 4000₺" yazılacak. 
"""

# isim = input("İsminizi giriniz: ")
# soyad = input("Soyadınız giriniz: ")
# yas = int(input("Yaşınızı giriniz: "))
# maas =int(input("Maaşınızı giriniz: "))
# cocuk_sayisi = int(input("Çocuk sayısını giriniz: "))
# if yas < 45 :
#   if cocuk_sayisi < 3:
#       maas += cocuk_sayisi*250
#   else:
#       maas += cocuk_sayisi*200
# else:
#     maas += cocuk_sayisi*500
# print(isim, soyad, "maaşınız:", maas)






