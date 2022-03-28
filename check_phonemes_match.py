from gruut import sentences
from lib_checker import *
from difflib import *
import re


#### Déclaration #####
    ## URLs des fichiers ##
source_insultes = './insulte2.txt'          #Fichier avec la liste d'insultes
    ## Variants ##
e_variants = ['é', 'è', 'ë','ê']            #Variants de la lettre e



insultes_array = get_no_variants(get_file_content(source_insultes), e_variants)
insultes_phonemes_array = get_phonemes_array(insultes_array)


##### Exec
print('Entrez un texte :')
input_str = input()
input_phonem = get_phoneme(input_str)
final = check_string_array_match(input_phonem, insultes_phonemes_array)

for k,v in final.items():
    print(k, ' : ', v)