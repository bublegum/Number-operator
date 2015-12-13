from tkinter import*

class Aplikacija():
    def __init__(self, master):

        menu = Menu(master)

        master.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label = "Možnosti", menu = file_menu)
        
        file_menu.add_command(label = "IZHOD", command = master.destroy)

        naslov = Label(text = "Vpiši številko!")
        naslov.grid(row = 0, columnspan = 2)

        napis1 = Label(text = "Vnesi število:")
        napis1.grid(row = 1, column = 0)

        self.vnos1 = StringVar(master, value = "")
        vnos1_polje = Entry(master, textvariable = self.vnos1)
        vnos1_polje.grid(row = 1, column = 1)

        gumb1 = Button(master, text = "potrdi!", command = self.kontrola)
        gumb1.grid(row = 2, column = 0)

        gumb2 = Button(master, text = "počisti polje!", command = self.pocisti)
        gumb2.grid(row = 2, column = 1)

        self.napis2 = StringVar(master, value = "")
        napis2_polje = Label(master, textvariable = self.napis2)
        napis2_polje.grid(row = 3, columnspan = 2)


    def potrdi(self):
        self.napis2.set("")
        self.izracuni()

    def pocisti(self):
        self.vnos1.set("")
        self.napis2.set("")

    def kontrola(self):
        sez = ["0","1","2","3","4","5","6","7","8","9"]
        for elt in self.vnos1.get():
            if elt not in sez:
                return self.opozorilo()
            else:
                pass
        return self.kontrola2()

    def opozorilo(self):
        self.napis2.set("Prosim vnesi zgolj številko!")

    def kontrola2(self):
        for elt in self.vnos1.get():
            if elt == "0":
                return self.opozorilo2()
            else:
                return self.potrdi()

    def opozorilo2(self):
        self.napis2.set("Prosim, naj se število ne začne z 0!")

    def izracuni(self):
        self.izbris_spomina()
        self.prvi_izpis()
        self.sodost()
        self.odgovori()
        self.izpis_vsote()
        self.collatz_len()
        self.deljitelji()
        self.novo_okno()

    def prvi_izpis(self):
        with open("app-spomin", "a", encoding = "utf8") as f:
            print("Izbrali ste število {0}.".format(self.vnos1.get()), file = f)

    def sodost(self):
        n = int(self.vnos1.get())
        if n % 2 == 0:
            with open("app-spomin", "a", encoding = "utf8") as f:
                print("Število {0} je sodo število.".format(self.vnos1.get()), file = f)
        else:
            with open("app-spomin", "a", encoding = "utf8") as f:
                print("Število {0} je liho število.".format(self.vnos1.get()), file = f)

    def je_prastevilo(self):
        n = int(self.vnos1.get())
        if n < 2:
            return False
        else:
            p = 2
            jealini = True
            while p*p <= n:
                if n % p == 0:
                    jealini = False
                    break
                p += 1
            if(jealini):
                return True
            else:
                return False

    def odgovori(self):
        a = int(self.vnos1.get())
        if self.je_prastevilo() == True:
            with open("app-spomin", "a", encoding = "utf8") as f:
                print("Število {0} je praštevilo.".format(self.vnos1.get()), file = f)
        else:
            with open("app-spomin", "a", encoding = "utf8") as f:
                print("Število {0} ni praštevilo.".format(self.vnos1.get()), file = f)

    def collatz_len(self):
        n = int(self.vnos1.get())
        counter = 1
        if n == 1:
            with open("app-spomin", "a", encoding = "utf8") as f:
                print("Dolžina Collatzovega zaporedja za število {0} je 1.".format(self.vnos1.get()), file = f)
        else:
            while n != 1:
                if n % 2 == 0:
                    n = n // 2
                    counter += 1
                else:
                    n = n*3 + 1
                    counter += 1
            with open("app-spomin", "a", encoding = "utf8") as f:
                print("Dolžina Collatzovega zaporedja za število {0} je {1}.".format(self.vnos1.get(), counter + 1), file = f)

    def deljitelji(self):
        n = int(self.vnos1.get())
        sez = []
        d = 1
        while d <= n:
            if n % d == 0:
                sez.append(d)
                d += 1
            else:
                d += 1
        with open("app-spomin", "a", encoding = "utf8") as f:
            if len(sez) <= 26:
                print("Seznam deljiteljev: {0}".format(sez), file = f)
                print("Število deljiteljev za število {0} je {1}.".format(self.vnos1.get(), len(sez)), file = f)
            else:
                print("Seznam deljiteljev je žal predolg za izpis.", file = f)
                print("Število deljiteljev za število {0} je {1}.".format(self.vnos1.get(), len(sez)), file = f)
        

    def vsota(self):
        x = int(self.vnos1.get())
        counter = 0
        sez = []
        while x>0:
            sez.append(x % 10)
            x = x//10
        for elt in sez:
            counter += elt
        return counter

    def izpis_vsote(self):
        with open("app-spomin", "a", encoding = "utf8") as f:
            print("Vsota števk za stevilo {1} je {0}.".format(self.vsota(), self.vnos1.get()), file = f)

    def novo_okno(self):
        novo_okno = Toplevel(root)
        novo_okno.title("Izpisi za število {0}".format(self.vnos1.get()))

        listbox = Listbox(novo_okno)
        listbox.grid(ipadx = 300)

        self.izpis_datoteke(listbox)

    def izpis_datoteke(self, listbox):
        with open("app-spomin", encoding = "utf8") as f:
            for vrstica in f:
                listbox.insert(END, str(vrstica))

    def izbris_spomina(self):
        with open("app-spomin", "wt", encoding = "utf8") as f:
            f.truncate()

root = Tk()
root.title("Aplikacija")
root.geometry("240x100")
aplikacija = Aplikacija(root)
root.mainloop()
