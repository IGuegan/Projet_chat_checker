from lib_checker import *
from time import process_time
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
dest = 'test.py'

"""--------------------------------
        Execution
--------------------------------"""

input_str = 'gros fils de pute salbatar enculé'

matchs = find_matchs_string_array(input_str, insultes_array)

toprint = 'detected = {'

for k,v in matchs.items():
    if v:
        toprint += '\n\t"' + k.replace('\n','') + '":\n\t{\n'
        # print(toprint)
        for cle, val in v.items():
                toprint += '\t\t"'+cle+'": '+str(val)+'\n'
                # print(toprint)
        # print('},')
        toprint += '\t}\n'
toprint_final = toprint.replace('\n\t\t"',',\n\t\t"').replace('{,','{').replace('}\n\n\t"','},\n\n\t"')
toprint_final += '}'
print(toprint_final)

destination_file = open(dest, "a", encoding="utf-16")
destination_file.write(toprint_final)
destination_file.close()
print(process_time())
