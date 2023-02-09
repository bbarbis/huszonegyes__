# megoldas
def pontszamitas(lapok):
    osszead = 0
    for i in range(len(lapok)):
        osszead += lapok[i]
        return osszead

def eredmeny(jatekos_L, gep_L):
    szoveg = ""
    jatekos = pontszamitas(jatekos_L)
    gep = pontszamitas(gep_L)
    if jatekos > 21:
        szoveg = "Játekos veszít"
    elif gep > 21:
        szoveg = "Gép veszít"


# esetek
def jatekosVesztettTeszt():
    jatekosLista = [4, 6, 11]
    gepLista = [3, 6, 9]
    print("\t \n Játékos:")
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("1. Játékos nyert")
    else:
        print("1. Játékos vesztett, 21 ponttal.")

def jatekosVesztettTeszt_2():
    jatekosLista = [3, 3, 3, 10]
    gepLista = [6, 9]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("2. Játékos nyert")
    else:
        print("2. Játékos vesztett több lapja van. ")

def jatekosVesztettTeszt_3():
    jatekosLista = [9, 10]
    gepLista = [6, 9, 10]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("3. Játékos nyert")
    else:
        print("3. Játékos vesztett, kevés lapja van. ")

def jatekos_NyertTeszt_4():
    jatekosLista = [6, 15]
    gepLista = [10, 11]
    if len(jatekosLista) < len(gepLista):
        print("4.Játékos nyert 21 ponttal")
    else:
        print("4. Játékos vesztett")

def jatekos_NyertTeszt_5():
    jatekosLista = [13, 15]
    gepLista = [5, 3, 1, 10]
    if len(jatekosLista) < len(gepLista):
        print("5. Játékos nyert 19 ponttal,de több lappal")
    elif len(jatekosLista) > len(gepLista):
        print("5. Játékos vesztett")

def jatekos_NyertTeszt_6():
    jatekosLista = [9, 8, 2]
    gepLista = [9, 10]
    if len(jatekosLista) > len(gepLista):
        print("6. Játékos nyert, 19 ponttal, de kevesebb lappal")
    else:
        print("6. Játékos vesztett")


def gep_VesztettTeszt_1():
    jatekosLista = [4, 15]
    gepLista = [4, 6, 11]
    print("\t \n Gép:")
    if len(jatekosLista) > len(gepLista):
        print("1. Gép nyert")
    else:
        print("1. Gép vesztett, 21 ponttal.")

def gep_VesztettTeszt_2():
    jatekosLista = [3, 10]
    gepLista = [3, 3, 3, 10]

    if len(jatekosLista) > len(gepLista):
        print("2. Gép nyert")
    else:
        print("2. Gép vesztett több lapja van. ")

def gep_VesztettTeszt_3():
    jatekosLista = [6, 9, 10]
    gepLista = [9, 10]
    if len(jatekosLista) < len(gepLista):
        print("3. Gép nyert")
    else:
        print("3. Gép vesztett, kevés lapja van. ")
def gep_NyertTeszt_4():
    jatekosLista = [15]
    gepLista = [10, 11]
    if len(jatekosLista) < len(gepLista):
        print("4.Gép nyert 21 ponttal")
    else:
        print("4. Gép vesztett 21 ponttal")
def gep_NyertTeszt_5():
    jatekosLista = [13, 15]
    gepLista = [5, 3, 1, 10]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    if len(jatekosLista) < len(gepLista):
        print("5. Gép nyert 19 ponttal,de több lappal")
    elif len(jatekosLista) > len(gepLista):
        print("5. Gép vesztett")

def gep_NyertTeszt_6():
    jatekosLista = [9, 8, 2]
    gepLista = [9, 10]


    if len(jatekosLista) > len(gepLista):
        print("6. Gép nyert, 19 ponttal, de kevesebb lappal")
    else:
        print("6. Nem jó a teszt")

def jatekos_gep_DontetlenTeszt_1():
    jatekosLista = [10, 11]
    gepLista = [10, 11]
    print("\t \n Döntetlen:")
    kapottEredmeny = eredmeny(jatekosLista, gepLista)

    if len(jatekosLista) == len(gepLista):
        print("1. Döntetlen, mind 2-nek 21-pontja van")
    else:
        print("1. Nem jó teszt")

def jatekos_gep_DontetlenTeszt_2():
    jatekosLista = [5, 5]
    gepLista = [4, 4]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)

    if len(jatekosLista) == len(gepLista):
        print("2. Döntetlen, egyforma lapok mennyisége")
    else:
        print("2. A teszt sikertelen állapotban van")

def jatekos_gep_DontetlenTeszt_3():
    jatekosLista = [3, 9, 10]
    gepLista = [3, 9, 10]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)

    if len(jatekosLista) == len(gepLista):
        print("3. Döntetlen, mind 2 meghaladta a 21-et")
    else:
        print("3. A teszt sikertelen állapotban van")
def tesztek():
    jatekosVesztettTeszt()
    jatekosVesztettTeszt_2()
    jatekosVesztettTeszt_3()

    jatekos_NyertTeszt_4()
    jatekos_NyertTeszt_5()
    jatekos_NyertTeszt_6()

    gep_VesztettTeszt_1()
    gep_VesztettTeszt_2()
    gep_VesztettTeszt_3()

    gep_NyertTeszt_4()
    gep_NyertTeszt_5()
    gep_NyertTeszt_6()

    jatekos_gep_DontetlenTeszt_1()
    jatekos_gep_DontetlenTeszt_2()
    jatekos_gep_DontetlenTeszt_3()

tesztek()