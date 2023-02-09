# megoldas
def pontszamitas(lapok):
    osszead = 0
    for i in range(len(lapok)):
        osszead += lapok[i]
        return osszead

def eredmeny(jatekos_L,gep_L):
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
    gepLista = [6, 9]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("1. Játékos nyert")
    else:
        print("1. Játékos vesztett.")

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
def jatekosVesztettTeszt_4():
    jatekosLista = [15]
    gepLista = [10, 11]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Gép nyert"
    if len(jatekosLista) < len(gepLista):
        print("4.Gép nyert 21 ponttal")
    else:
        print("4. Gép vesztett 21 ponttal")
def jatekosVesztettTeszt_5():
    jatekosLista = [13, 15]
    gepLista = [5, 3, 1, 10]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Gép nyert"
    if len(jatekosLista) < len(gepLista):
        print("5. Gép nyert 19 ponttal,de több lappal")
    elif len(jatekosLista) > len(gepLista):
        print("5. Gép vesztett")

def jatekosVesztettTeszt_6():
    jatekosLista = [9, 8, 2]
    gepLista = [9, 10]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Gép nyert"
    if len(jatekosLista) > len(gepLista):
        print("6. Gép nyert, 19 ponttal, de kevesebb lappal")
    else:
        print("6. Nem jó a teszt")

def jatekos_gep_DontetlenTeszt_7():
    jatekosLista = [10, 11]
    gepLista = [10, 11]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if len(jatekosLista) == len(gepLista):
        print("7. Döntetlen, mind 2-nek 21-pontja van")
    else:
        print("7. Nem jó teszt")

def jatekos_gep_DontetlenTeszt_8():
    jatekosLista = [5, 5]
    gepLista = [4, 4]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if len(jatekosLista) == len(gepLista):
        print("8. Döntetlen, egyforma lapok mennyisége")
    else:
        print("8. A teszt sikertelen állapotban van")

def jatekos_gep_DontetlenTeszt_9():
    jatekosLista = [3, 9, 10]
    gepLista = [3, 9, 10]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if len(jatekosLista) == len(gepLista):
        print("8. Döntetlen, mind 2 meghaladta a 21-et")
    else:
        print("8. A teszt sikertelen állapotban van")
def tesztek():
    jatekosVesztettTeszt()
    jatekosVesztettTeszt_2()
    jatekosVesztettTeszt_3()
    jatekosVesztettTeszt_4()
    jatekosVesztettTeszt_5()
    jatekosVesztettTeszt_6()
    jatekos_gep_DontetlenTeszt_7()
    jatekos_gep_DontetlenTeszt_8()
    jatekos_gep_DontetlenTeszt_9()

tesztek()