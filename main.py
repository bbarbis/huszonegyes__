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
    jatekosLista = [4, 6, 8]
    gepLista = [6, 9]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("1. Játékos nyert")
    else:
        print("1. Játékos vesztett.")

def jatekosVesztettTeszt_2():
    jatekosLista = [3, 6, 8, 10]
    gepLista = [6, 9]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("2. Játékos nyert")
    else:
        print("2. Játékos vesztett több lapja van. ")

def jatekosVesztettTeszt_3():
    jatekosLista = [9, 10, 2, 8]
    gepLista = [6, 9, 10]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("3. Játékos nyert")
    else:
        print("3. Játékos vesztett, 5 lapja van. ")
def jatekosVesztettTeszt_4():
    jatekosLista = [15]
    gepLista = [7, 9]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if len(jatekosLista) > len(gepLista):
        print("4. Játékos nyert")
    else:
        print("4. Játékos vesztett, nagy lapja van. ")
def jatekosVesztettTeszt_5():
    jatekosLista = [2, 8, 10]
    gepLista = [5, 9]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if len(jatekosLista) == len(gepLista):
        print("5. Játékos nyert")
    elif len(jatekosLista) == len(gepLista):
        print("5. Játékos vesztett")
    else:
        print("5. Döntetlen. ")

def jatekosVesztettTeszt_6():
    jatekosLista = [5, 7, 9]
    gepLista = [2, 5, 7]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if len(jatekosLista) == len(gepLista):
        print("6. Döntetlen. ")
    else:
        print("6. Nem jó a teszt")

def jatekosVesztettTeszt_7():
    jatekosLista = [4, 5, 7]
    gepLista = [5, 8]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("7. Játékos nyert")
    else:
        print("7. Játékos vesztett. ")

def jatekosVesztettTeszt_8():
    jatekosLista = [3, 6, 8, 10]
    gepLista = [6, 9]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if len(jatekosLista) == len(gepLista):
        print("8. A teszt sikertelen állapotban van")
    else:
        print("8. A teszt sikertelen állapotban van")
def tesztek():
    jatekosVesztettTeszt()
    jatekosVesztettTeszt_2()
    jatekosVesztettTeszt_3()
    jatekosVesztettTeszt_4()
    jatekosVesztettTeszt_5()
    jatekosVesztettTeszt_6()
    jatekosVesztettTeszt_7()
    jatekosVesztettTeszt_8()

tesztek()