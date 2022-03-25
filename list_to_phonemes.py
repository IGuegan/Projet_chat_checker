from dataclasses import replace
import readline
from gruut import sentences

text = 'Fils de pute'

# Récupération des mots dans le fichier 'insulte.txt'
fichier = './insulte2.txt'
result = open(fichier, "r")
all_lines = result.readlines()
result.close()


list_line = []

#Déclaration des variantes de sonorités pour chaque caractère
e_variants = ['é', 'è', 'ë','ê']
#Juste compléter ici les listes de variantes des sonorités ressemblantes

#Pour chaque ligne du fichier
for line in all_lines:
    line_tmp = line.replace('\n', '') #Retrait du retour chariot
    #Boucle pour remplacer toutes les variantes de chaque lettre qui ont une pronociation proche
    for e_variant in e_variants:
        line_tmp = line.replace(e_variant, 'e')

    list_line.append(line_tmp)


# Transformation et ecriture des insultes dans le fichier 'insulte_phonetic.txt'
file_insulte_ph = open("./insulte_phonetic.txt", "a")

#Pour chaque ligne
for line in list_line:
    #
    for sent in sentences(line, lang="fr"):
        phrase = ''
        for line_ph in sent:
            if line_ph.phonemes:
                line_string = ''.join(line_ph.phonemes)
                phrase = phrase + line_string
    print(phrase + '\n')
    file_insulte_ph.write(phrase + '\n')

file_insulte_ph.close()