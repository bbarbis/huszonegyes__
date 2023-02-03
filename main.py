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
    jatekosLista = [6, 4, 8, 9]
    gepLista = [6, 4, 11]

    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos veszített"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :)")
    # jatekosnak nagyobb a lapja mint a gépnek
    if len(jatekosLista) > len(gepLista):
        print("Játékosnak több lapja van.")
    

def tesztek():
    jatekosVesztettTeszt()

tesztek()