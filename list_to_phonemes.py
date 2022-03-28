from lib_checker import *

"""--------------------------------
        Déclarations
--------------------------------"""
    ## URLs des fichiers ##
source_insultes = './insulte2.txt'          #Fichier avec la liste d'insultes
destination_phonemes = './phonemes.txt'     #Fichier destination pour la liste des phonemes
    ## Variants ##
e_variants = ['é', 'è', 'ë','ê','3']            #Variants de la lettre e


"""--------------------------------
        Execution
--------------------------------"""
all_lines = get_file_content(source_insultes)
all_lines = get_no_variants(all_lines, e_variants)
destination_file = open(destination_phonemes, "a", encoding="utf-8")
res = get_phonemes(all_lines)
print(res)
destination_file.write(res)
destination_file.close()