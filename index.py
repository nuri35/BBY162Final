from tkinter import  *
from tkinter import messagebox
import time
from tkinter import filedialog








bilgiler = ["yazılım", "12345"]


denemeHakkı = 3
zaman = 0

pencere = Tk()




pencere.iconbitmap(r'file.png')

photo = PhotoImage(file="resim_03.gif")
resim = Label(pencere,image=photo)
resim.pack()



pencere.title("hacettepe kütüphanesi")

pencere.geometry("550x350+350+50")









yazı = Label(pencere)
yazı.config(text = "uygulamaya hoşgeldiniz")
yazı.pack()



kAdıSor = Label(pencere)
kAdıSor.config(text="kullanıcı adı:", bg="blue", fg="white", font=("Calibri Italic", 12))
kAdıSor.pack()

kAdıAl = Entry(pencere)
kAdıAl.pack()

şifreSor = Label(pencere)
şifreSor.config(text="şifre:", bg="blue", fg="white", font=("Calibri Italic", 16))
şifreSor.pack()

şifreAl = Entry(pencere,  width="8", show="*")
şifreAl.pack()



sifremihatirla = Checkbutton(pencere, text="şifremi hatırla")
sifremihatirla.pack()

kntrl = Label(pencere)
kntrl.config(text="henüz sisteme giriş yapılmadı.")
kntrl.pack()


def gir():
    global denemeHakkı, zaman

    if denemeHakkı<= 0:
        if time.time()-zaman  >= 5:
            denemeHakkı = 3
        else:
            sonuc.config(text="zaman aşımı 5 saniye bekle.")
        return False


    kAdı = kAdıAl.get()
    şifre = şifreAl.get()
    print (kAdı, " - ", şifre)
    print("bilgiler kontrol ediliyor sistem tarafından")

    if kAdı == bilgiler[0] and şifre == bilgiler[1]:
        print("hacettepe kataloğuna giriş yapıldı")
        sonuc.config(text="henüz giriş yapılmadı")
        yenialan()


    elif kAdı != bilgiler[0] and şifre == bilgiler[1]:
        print("kullanıcı adı hatalı")
        denemeHakkı -= 1
        if denemeHakkı == 0:
            zaman = time.time()
        sonuc.config(text="bilgiler yanlış! kalan deneme: %d" % denemeHakkı)
        kntrl.config(text="kullanıcı adınız yanlış.")
    elif kAdı == bilgiler[0] and şifre != bilgiler[1]:
        print("Şifre hatalı")
        denemeHakkı -= 1
        if denemeHakkı == 0:
            zaman = time.time()
        sonuc.config(text="bilgiler yanlış! kalan deneme: %d" % denemeHakkı)
        kntrl.config(text="Şifreniz hatalı")



    else:
        print("bilgiler yanlıs!")
        denemeHakkı -= 1
        if denemeHakkı == 0:
            zaman = time.time()
        sonuc.config(text="bilgiler yanlış! kalan deneme: %d" %denemeHakkı)






girtuş = Button(pencere)
girtuş.config(text="giriş yap", bg="blue", fg="white", activebackground="blue",
              activeforeground="white", font=("Calibri", 12), command=gir)
girtuş.pack()

sonuc = Label(pencere)
sonuc.config(text = "henüz giriş yapılmadı")
sonuc.pack()

çıktuş = Button(pencere)
çıktuş.config(text="Uygulamadan Çık", bg="blue", fg="white", activebackground="blue",
              activeforeground="white", font=("Calibri", 12), command=pencere.destroy)

def yenialan():

    def katalog_listeleri():
        pencerex = Tk()
        pencerex.configure(background="white")




        cıkıs = Button(pencerex, text="Kapat", command=pencerex.destroy, fg="white", bg="blue", cursor="man")
        cıkıs.pack()

    global kitap, kitapadıalanı
    global yazaradı, yazaradıalanı
    global yıl, yayınyılı

    anaSayfa = Tk()
    anaSayfa.title("Elektronik Kataloğ taraması")

    anaSayfa.configure(background="lightblue")
    anaSayfa.geometry("550x350+350+50")
    anaSayfa.resizable(0, 0)
    giriş = Label(anaSayfa,
                  text="kataloğ sistemine giriş başaarılı   \n  aramak istediğiniz karakteri giriniz",
                  bg="lightblue", fg="brown", font=("Calibri Italic", 19)).grid()

    kitapadıalanı = ["Makina bilgisi : makine bilgisine giriş", "Industrial automation and robotics", "çalıkuşu",
                     "Tuhaf kütüphane"]
    yazaradıalanı = ["Akkurt, Mustafa", "Gupta, A. K", "reşat nuri güntekin", "Murakami, Haruki"]
    yayınyılı = ["2011", "2007", "1942", "1949"]

    kitaparama = Label(anaSayfa, text="aramak istediğiniz kitap adı:", bg="lightblue", fg="white",
                       font=("Calibri Italic", 13)).grid()
    kitap = Entry(anaSayfa,width=27)
    kitap.grid()
    aramabutonu = Button(anaSayfa, text="ARA", bg="white", fg="black", font=("calibri", 10), cursor="star",
                         command=giris1).grid()

    kitaparama = Label(anaSayfa, text="aramak istediğiniz eser adı:", bg="lightblue", fg="white",
                       font=("Calibri Italic", 13)).grid()
    yazaradı = Entry(anaSayfa, width=27)
    yazaradı.grid()
    aramabutonu = Button(anaSayfa, text="ARA", bg="white", fg="black", font=("calibri", 10), cursor="star",
                         command=giris2).grid()

    kitaparama = Label(anaSayfa, text="aramak istediğiniz yayın yılı :", bg="lightblue", fg="white",
                       font=("Calibri Italic", 13)).grid()
    yıl = Entry(anaSayfa, width=27)
    yıl.grid()
    aramabutonu = Button(anaSayfa, text="ARA", bg="white", fg="black", font=("calibri", 10), cursor="star",
                         command=giris3).grid()


    cikis = Button(anaSayfa, text="Kapat", command=exit, fg="black", bg="white", cursor="man")
    cikis.grid()




def giris3():
    yılı = yıl.get()

    if yılı == yayınyılı[0]:
        messagebox.showinfo("katalog sistemindeki kitap", "KİTAP ADI:Makina bilgisi : makine bilgisine giriş  \n YAZAR ADI: Akkurt, Mustafa \n YAYIN YILI: 2011")

    elif yılı ==yayınyılı[1]:
        messagebox.showinfo("katalog sistemindeki kitap", "KİTAP ADI: Industrial automation and robotics \n YAZAR ADI: Gupta, A. K \n YAYIN YILI: 2007")



    elif yılı == yayınyılı[2]:
        messagebox.showinfo("katalog sistemindeki kitap","KİTAP ADI: ÇALIKUŞU \n YAZAR ADI: REŞAT NURİ GÜNTEKİN \n TÜR:ROMAN \n YAYIN YILI: 1942")

    elif yılı == yayınyılı[3]:
        messagebox.showinfo("katalog sistemindeki kitap","KİTAP ADI: Tuhaf kütüphane \n YAZAR ADI: Murakami, Haruki  \n YAYIN YILI: 1949")
    else:
        soru = messagebox.showerror("hatakodu04xx234","Aradığınız kaynak katalog kaydında bulunmamaktadır. ")



def giris2():
    yaz = yazaradı.get()

    if yaz == yazaradıalanı[0]:
        messagebox.showinfo("katalog sistemindeki kitap", "KİTAP ADI:Makina bilgisi : makine bilgisine giriş  \n YAZAR ADI: Akkurt, Mustafa \n YAYIN YILI: 2011")

    elif yaz ==yazaradıalanı[1]:
        messagebox.showinfo("katalog sistemindeki kitap", "KİTAP ADI: Industrial automation and robotics \n YAZAR ADI: Gupta, A. K \n YAYIN YILI: 2007")

    elif yaz == yazaradıalanı[2]:
        messagebox.showinfo("katalog sistemindeki kitap","KİTAP ADI: ÇALIKUŞU \n YAZAR ADI: REŞAT NURİ GÜNTEKİN \n TÜR:ROMAN \n YAYIN YILI: 1942")

    elif yaz == yazaradıalanı[3]:
        messagebox.showinfo("katalog sistemindeki kitap","KİTAP ADI: Tuhaf kütüphane \n YAZAR ADI: Murakami, Haruki  \n YAYIN YILI: 1949")
    else :
        soru = messagebox.showerror("hatakodu03244xx234","Aradığınız kaynak katalog kaydında bulunmamaktadır. ")

def giris1():
    adı = kitap.get()

    if adı == kitapadıalanı[0]:

        messagebox.showinfo("katalog sistemindeki kitap", "KİTAP ADI:Makina bilgisi : makine bilgisine giriş  \n YAZAR ADI: Akkurt, Mustafa \n YAYIN YILI: 2011")

    elif adı == kitapadıalanı[1]:
        messagebox.showinfo("katalog sistemindeki kitap", "KİTAP ADI: Industrial automation and robotics \n YAZAR ADI: Gupta, A. K \n YAYIN YILI: 2007")

    elif adı == kitapadıalanı[2]:
        messagebox.showinfo("katalog sistemindeki kitap","KİTAP ADI: ÇALIKUŞU \n YAZAR ADI: REŞAT NURİ GÜNTEKİN \n YAYIN YILI: 1942")

    elif adı == kitapadıalanı[3]:
        messagebox.showinfo("katalog sistemindeki kitap","KİTAP ADI: Tuhaf kütüphane \n YAZAR ADI: Murakami, Haruki  \n YAYIN YILI: 1949")
    else:
        soru = messagebox.showerror("hatakodu04x32322x234","Aradığınız kaynak katalog kaydında bulunmamaktadır. ")


mainloop()



