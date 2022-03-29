from lib_checker import *

"""--------------------------------
        Déclaration
--------------------------------"""

## URLs des fichiers ##
source_insultes = './insulte2.txt'          # Fichier avec la liste d'insultes

## Variants ##
e_variants = ['é', 'è', 'ë', 'ê', '&']            # Variants de la lettre e

## Ponctuation ##
ponctuations = ['?', ':', ';', ',', '/', '!', '§', '%', '¨', '^', '$', '£', '¤', '"',
                "'", '#', '{', '(', '[', '-', '|', '`', '_', '\\', '^', ')', ']', '=', '+', '}', '*']

"""--------------------------------
        Initialisation
--------------------------------"""

# Récupération des insultes du fichier, et remplacement des variantes de lettres
insultes_array = clean_text(get_file_content(source_insultes), e_variants, ponctuations)
# Récupération des phonétiques des insultes
insultes_phonemes_array = get_phonemes_array(insultes_array)


"""--------------------------------
        Execution
--------------------------------"""

input_str = 'eh salut, véronique ta mère ? gros fils de pute salbatar'

matchs = find_matchs_string_array(input_str, insultes_array)

for k,v in matchs.items():
    if v:
        print('{',k.replace('\n',''),':\n{')
        for cle, val in v.items():
            print('\t{',cle,': \'',val,'\'}')
        print('}\n},')
