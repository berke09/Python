import cv2
import datetime
import time


def open_foto(uzantı):
    adres = "C:\\Users\\Abra v15.8\\Desktop\\oc.resimler\\{}".format(uzantı)
    foto = cv2.imread(adres)
    cv2.imshow("pencere",foto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def convert2gray(uzantı):
    adres = "C:\\Users\\Abra v15.8\\Desktop\\oc.resimler\\{}".format(uzantı)
    foto = cv2.imread(adres)
    gray = cv2.cvtColor(foto,cv2.COLOR_BGR2GRAY)
    cv2.imshow("pencere",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def live_video():
    cam = cv2.VideoCapture(0)
    fourc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("C:\\Users\\Abra v15.8\\Desktop\\oc.resimler\\video_izle.avi",fourc,30.0,(640,480))
    while cam.isOpened():
        ret,frame = cam.read()
        cv2.putText(frame,str(datetime.datetime.now()),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        out.write(frame) # önce kayıt edildi sonra gösterildi diğer türlü hata verir.
        cv2.imshow("pencere",frame)
        if cv2.waitKey(1) & 0xFF == ord("q"): # q ile kapanır
            break
    cam.release()
    cv2.destroyAllWindows()


def proporties_of_foto(uzantı):
    adres = "C:\\Users\\Abra v15.8\\Desktop\\oc.resimler\\{}".format(uzantı)
    foto = cv2.imread(adres)
    a,b,c = foto.shape
    print("fotoğrafın genişliği : {}\nfotoğrafın yüksekliği : {}\nfotoğrafın renk boyutu : {}".format(a,b,c))
    print("fotoğrafın type ı : " + "{}".format(foto.dtype))

def proporties_of_video(uzantı):
    
    live_or_not = int(input("1-canlı video için 1'e basınız.\n2-eski video için 2'e basınız.\nSeçiminiz : "))
    adres = "C:\\Users\\Abra v15.8\\Desktop\\oc.resimler\\{}".format(uzantı)

    if live_or_not == 1:  # video is lives
        cam = cv2.VideoCapture(0)
        print(cam.get(3))
        print(cam.get(4))

        while cam.isOpened():
            ret,frame = cam.read()
            cv2.imshow("pencere",frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):  # q ile kapanır
                break
        cam.release()
        cv2.destroyAllWindows()

    else : # vide was created in pass 
        cam = cv2.VideoCapture(adres)
        print(cam.get(3))
        print(cam.get(4))
        while True:
            ret,frame = cam.read()
            cv2.imshow("pencere",frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cam.release()
        cv2.destroyAllWindows()
def taking_a_foto():
    cam = cv2.VideoCapture(0)
    i=0
    while cam.isOpened() & i<=0:
        take = int(input("fotoğraf çekmek için 1'e basınız : "))
        if take == 1:
            ret,frame = cam.read()
            cv2.imshow("pencere",frame)
            print("fotoğraf başarılı şekilde çekildi")  
            cv2.waitKey(0)
            cam.release()
            cv2.destroyAllWindows()
            break
        else:
            break

# MAİN PROGRAM..

try:
    while True:
        print("********************************************** UYGULAMAMIZA HOSGELDİNİZ ************************************************\n".center(50))
        secim = int(input("1-istenen fotoğrafı görmek için 1'e basınız.\n2-istenen fotoğrafı siyah beyaz yapmak için 2'e basınız.\n3-video çekmek için 3'e basınız.\n4-istenen fotoğrafın özelliklerini öğrenmek için 4'e basınız.\n5-Canlı veya eski videonun özelliklerini öğrenmek için 5'e basınız.\n6-fotoğraf çekmek için 6 'ya basınız\n7-Çıkış için 7'ya basınız.\nSeçiminiz : "))

        if secim == 1:
            print("yönlendiriliyorsunuz.")
            time.sleep(0.3)
            uzantı = input("\nistenen fotoğrafın uzantısı ve ismini düzgün bir şekilde giriniz.\nUzantı: ")
            try:
                print("fotoğraf açılıyor")
                time.sleep(0.2)
                open_foto(uzantı)
            except:
                print("girdiğniz adreste bir fotoğraf bulunamadı.\n")
                secim = input("Tekrar çalıştırmak isterseniz 'T' ye basınız.\nSeçim : ")
                
                if secim == "T":
                    print("Ana menüye yönlendiriliyorsunuz")
                    time.sleep(0.25)
                else:
                    print("program sonlandırılıyor.Lütfen bekleyiniz")
                    time.sleep(1)
                    break
            else:
                print("işlem sona erdi.\n")
                time.sleep(0.2)
                tekrar = input("\nEğer tekrar ana menüye dönmek istiyorsanız 'E' basınız.\nEğer istemyiyorsanız herhangi bir tuşa basınız.\nSeçiminiz : ")
                if tekrar == "E":
                    pass
                else:
                    print("*****tekrar bekleriz*****")
                    time.sleep(0.5)
                    break
            finally :
                pass         
                    
        elif secim ==2:
            print("yönlendiriliyorsunuz.")
            time.sleep(0.3)
            uzantı = input("\nistenen fotoğrafın uzantısını ve ismini düzgün bir şekilde giriniz.\nUzantı : ")
            try:
                print("fotoğraf açılıyor")
                time.sleep(0.2)
                convert2gray(uzantı)
            except:
                print("girdiğniz adreste bir fotoğraf bulunamadı.\n")
                secim = input("Tekrar çalıştırmak isterseniz 'T' ye basınız.\nSeçim : ")
                
                if secim == "T":
                    print("Ana menüye yönlendiriliyorsunuz")
                    time.sleep(0.25)
                else:
                    print("program sonlandırılıyor.Lütfen bekleyiniz")
                    time.sleep(1)
                    break
            else:
                print("işlem sona erdi.\n")
                time.sleep(0.2)
                tekrar = input("\n\nEğer tekrar ana menüye dönmek istiyorsanız 'E' basınız.\nEğer istemyiyorsanız herhangi bir tuşa basınız.\nSeçiminiz : ")
                if tekrar == "E":
                    pass
                else:
                    print("*****tekrar bekleriz*****")
                    time.sleep(0.5)
                    break
            finally :
                pass
    
        elif secim ==3:
            try:
                print("yönlendiriliyorsunuz.")
                time.sleep(0.3)
                print("video açılıyor")
                time.sleep(0.5)
                live_video()            
            except:
                print("bir şeyler yanlış gitti video okunamıyor\n")
                secim = input("Tekrar çalıştırmak isterseniz 'T' ye basınız.\nSeçim : ")
                
                if secim == "T":
                    print("Ana menüye yönlendiriliyorsunuz")
                    time.sleep(0.25)
                else:
                    print("program sonlandırılıyor.Lütfen bekleyiniz")
                    time.sleep(1)
                    break
            else:
                print("işlem sona erdi.\n")
                time.sleep(0.2)
                tekrar = input("\nEğer tekrar ana menüye dönmek istiyorsanız 'E' basınız.\nEğer istemyiyorsanız herhangi bir tuşa basınız.\nSeçiminiz : ")
                if tekrar == "E":
                    pass
                else:
                    print("*****tekrar bekleriz*****")
                    time.sleep(0.5)
                    break
            finally:
                pass


        elif secim ==4:
            print("yönlendiriliyorsunuz.")
            time.sleep(0.3)
            uzantı = input("\nistenen fotoğrafın uzantısını ve ismini düzgün bir şekilde giriniz.\nUzantı : ")
            try:
                print("Özellikler getiriliyor.\n")
                time.sleep(0.2)
                proporties_of_foto(uzantı)
            except:
                print("bir şeyler yanlış gitti.\n")
                secim = input("Tekrar çalıştırmak isterseniz 'T' ye basınız.\nSeçim : ")
                
                if secim == "T":
                    print("Ana menüye yönlendiriliyorsunuz")
                    time.sleep(0.25)
                else:
                    print("program sonlandırılıyor.Lütfen bekleyiniz")
                    time.sleep(1)
                    break
            else:
                print("işlem sona erdi.\n")
                time.sleep(0.2)
                tekrar = input("\nEğer tekrar ana menüye dönmek istiyorsanız 'E' basınız.\nEğer istemyiyorsanız herhangi bir tuşa basınız\nSeçiminiz : ")
                if tekrar == "E":
                    pass
                else:
                    print("*****tekrar bekleriz*****")
                    time.sleep(0.5)
                    break
            finally:
                pass
            
        elif secim ==5:
            print("yönlendiriliyorsunuz.")
            time.sleep(0.3)
            uzantı = input("\nvideonun adresini düzgün şekilde giriniz .\nEğer yeni bir video oluşturmak istiyorsanız herhangi bir tuşa basınız basınız.\nUzantı : ")
            try:
                print("özellikler getiriliyor\n")
                time.sleep(0.2)
                proporties_of_video(uzantı)
            except:
                print("bir şeyler yanlış gitti.")
                secim = input("Tekrar çalıştırmak isterseniz 'T' ye basınız.\nSeçim : ")

                if secim == "T":
                    print("Ana menüye yönlendiriliyorsunuz")
                    time.sleep(0.25)
                else:
                    print("program sonlandırılıyor.Lütfen bekleyiniz")
                    time.sleep(1)
                    break
            else:
                print("işlem sona erdi.\n")
                time.sleep(0.2)
                tekrar = input("\nEğer tekrar ana menüye dönmek istiyorsanız 'E' basınız.\nEğer istemyiyorsanız herhangi bir tuşa basınız.\nSeçiminiz : ")
                if tekrar == "E":
                    pass
                else:
                    print("*****tekrar bekleriz*****")
                    time.sleep(0.5)
                    break
            finally:
                pass

        elif secim ==6:
            try:
                print("yönlendiriliyorsunuz.")
                time.sleep(0.3)
                taking_a_foto()
            except:
                print("bir şeyler yanlış gitti.")
                secim = input("Tekrar çalıştırmak isterseniz 'T' ye basınız.\nSeçim : ")
                
                if secim == "T":
                    print("Ana menüye yönlendiriliyorsunuz")
                    time.sleep(0.25)
                else:
                    print("program sonlandırılıyor.Lütfen bekleyiniz")
                    time.sleep(1)
                    break
            else:
                print("işlem sona erdi.\n")
                time.sleep(0.2)
                tekrar = input("\nEğer tekrar ana menüye dönmek istiyorsanız 'E' basınız.\nEğer istemyiyorsanız herhangi bir tuşa basınız.\nSeçiminiz : ")
                if tekrar == "E":
                    pass
                else:
                    print("*****tekrar bekleriz*****")
                    time.sleep(0.5)
                    break
            finally:
                pass
        else:
            print("tekrar bekleriz")
            break
except:
    print("\nProgram yeniden çalıştırılırken bir hata oldu.")
    print("F5'e basarak yeniden çalıştırmayı deneyebilir veya daha sonra tekrar deneyebilirsiniz.")