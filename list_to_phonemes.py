from gruut import sentences

# Récupération des mots dans le fichier 'insulte.txt'
def get_file_content(fic_url):
    result = open(fic_url, "r")
    all_lines= result.readlines()
    result.close()
    return all_lines

#Remplacement de tous les variants
#   paramètre : all_lines -> 
def get_no_variants(all_lines):
    list_line = []
    for line in all_lines:
        line_tmp = line.replace('\n', '') #Retrait du retour chariot
        #Boucle pour remplacer toutes les variantes de chaque lettre qui ont une pronociation proche
        for e_variant in e_variants:
            line_tmp = line.replace(e_variant, 'e')

        list_line.append(line_tmp)
    return(list_line)

def get_phonemes(data):
    result = ''
    for line in data:
        for sent in sentences(line, lang="fr"):
            phrase = ''
            for line_ph in sent:
                if line_ph.phonemes:
                    line_string = ''.join(line_ph.phonemes)
                    phrase = phrase + line_string
        result = result + phrase + '\n' 
    return result


#### Déclaration #####
    ## URLs des fichiers ##
source_insultes = './insulte2.txt'          #Fichier avec la liste d'insultes
destination_phonemes = './phonemes.txt'     #Fichier destination pour la liste des phonemes

    ## Variants ##
e_variants = ['é', 'è', 'ë','ê']            #Variants de la lettre e



##### Execution ######
all_lines = get_file_content(source_insultes)
all_lines = get_no_variants(all_lines)
destination_file = open(destination_phonemes, "a", encoding="utf-8")
res = get_phonemes(all_lines)
print(res)
destination_file.write(res)
destination_file.close()