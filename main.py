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
        print("Játékos nyert")
    else:
        print("Játékos vesztett.")

def jatekosVesztettTeszt_2():
    jatekosLista = [3, 6, 8, 10]
    gepLista = [6, 9]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("Játékos nyert")
    else:
        print("Játékos vesztett több lapja van. ")

def jatekosVesztettTeszt_3():
    jatekosLista = [3, 6, 8, 10]
    gepLista = [6, 9]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("Játékos nyert")
    else:
        print("Játékos vesztett több lapja van. ")



def tesztek():
    jatekosVesztettTeszt()
    jatekosVesztettTeszt_2()
    jatekosVesztettTeszt_3()

tesztek()