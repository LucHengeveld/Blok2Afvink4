import re
import time


def opdr1():
    """ Opent een fasta bestand en verdeeld dit in 2 lijsten, een lijst met
    daarin alle headers en een lijst met daarin alle eiwitten. Hierna word
    gekeken en geprint of de letter B wel of niet voorkomt. Ook word er gekeken
    of de consensus voorkomt in de lijst met eiwitten.
    """
    bestand = open("Mus_musculus.GRCm38.pep.all.fa", "r")
    lijst = []
    lijst2 = []
    for regel in bestand:
        if ">" in regel:
            lijst.append(regel)
        if ">" not in regel:
            lijst2.append(regel)

    x = 0
    for i in range(len(lijst2)):
        letterB = re.findall("B", lijst2[i])
        if (letterB):
            x += 1
    if x > 0:
        print("De letter B komt wel voor")
    else:
        print("De letter B komt niet voor")

    x = 0
    for i in range(len(lijst)):
        consensus = re.findall("MCNSSC[MV]GGMNRR", lijst2[i])
        if (consensus):
            print("Het patroon komt hierin voor:", lijst[i], lijst2[i])


def opdr2():
    """Verdeeld het bestand in twee lijsten, headers en sequenties. Er word
    gekeken of het zuiver DNA is met behulp van een regular expression en een
    iteratieve functie en dit word geprint.
    Ook word de tijd van het process bijgehouden
    """
    bestand = open("Mus_musculus.GRCm38.dna.chromosome.1.fa", "r")
    lijst = []
    lijst2 = []
    for regel in bestand:
        if "\n" in regel:
            regel.replace("\n", "")
        if ">" in regel:
            lijst.append(regel)
        if ">" not in regel:
            lijst2.append(regel)

    start = time.time()
    x = 0
    for i in range(100):
        DNA = re.findall("ACTGN", lijst2[i])
        if not (DNA):
            x += 1
    if x > 0:
        print("Dit is geen zuiver DNA")
    print("Regular expression duurde", time.time() - start, "seconden")

    start = time.time()
    string = "ACTGN"
    for i in range(100):
        x = lijst2[i].find(string)
    if not x > 0:
        print("Dit is geen zuiver DNA")
    print("Iteratieve functie duurde", time.time() - start, "seconden")


def opdr3():
    return


def main():
    """Vraagt welke opdracht je wilt starten (opdr1 of opdr 2) en start de
    bijbehorende functie.
    """
    opdr = input("Welke opdr wil je starten? opdr1 / opdr2 ")
    if opdr == "opdr1":
        opdr1()
    if opdr == "opdr2":
        opdr2()


main()
