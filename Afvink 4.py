##########################################################################
# (c) 2013 HAN/Martijn van der Bruggen                                   #
# Dictionaries voor het gebruik bij de afvinkopdrachten van HBI-Cou3a    #
# Update: 24-feb-2013 voorzien van commentaar en bestandsnaam aangepast  #
##########################################################################

def afvink3():
    triplet = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
               'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
               'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
               'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
               'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
               'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
               'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
               'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
               'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
               'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
               'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
               'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
               'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
               'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
               'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
               'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
               }

    eiwitten = {"Ala": ["GCU", "GCC", "GCA", "GCG"],
                "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
                "Asn": ["AAU", "AAC"],
                "Asp": ["GAU", "GAC"],
                "Cys": ["UGU", "UGC"],
                "Gln": ["CAA", "CAG"],
                "Glu": ["GAA", "GAG"],
                "Gly": ["GGU", "GGC", "GGA", "GGG"],
                "His": ["CAU", "CAC"],
                "Ile": ["AUU", "AUC", "AUA"],
                "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
                "Lys": ["AAA", "AAG"],
                "Met": ["AUG"],
                "Phe": ["UUU", "UUC"],
                "Pro": ["CCU", "CCC", "CCA", "CCG"],
                "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
                "Thr": ["ACU", "ACC", "ACA", "ACG"],
                "Trp": ["UGG"],
                "Tyr": ["UAU", "UAC"],
                "Val": ["GUU", "GUC", "GUA", "GUG"],
                "Start": ["AUG", "CUG", "UUG", "GUG", "AUU"],
                "Stop": ["UAG", "UGA", "UAA"]
                }

    dnaseq = input("Geef een RNA sequentie: ")
    dnaseq = dnaseq.lower()
    lijst = dnaseq.replace("", " ").split(" ")
    lijst.remove("")
    lijst.pop(-1)

    i = 0
    lijst2 = []

    while i < len(lijst):
        een = i
        twee = i+1
        drie = i+2
        string = lijst[een] + lijst[twee] + lijst[drie]
        lijst2.append(string)
        i += 3

    lijst3 = []
    i = 0
    while i < len(lijst2):
        lijst3.append(triplet[lijst2[i]])
        i += 1

    print(lijst3)

def main():
    afvink3()

main()