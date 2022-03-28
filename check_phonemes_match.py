from lib_checker import *

"""--------------------------------
        Déclaration
--------------------------------"""

    ## URLs des fichiers ##
source_insultes = './insulte2.txt'          # Fichier avec la liste d'insultes
    ## Variants ##
e_variants = ['é', 'è', 'ë','ê']            # Variants de la lettre e


"""--------------------------------
        Initialisation
--------------------------------"""

insultes_array = get_no_variants(get_file_content(source_insultes), e_variants)     # Récupération des insultes du fichier, et remplacement des variantes de lettres
insultes_phonemes_array = get_phonemes_array(insultes_array)                        # Récupération des phonétiques des insultes


"""--------------------------------
        Execution
--------------------------------"""

print('Entrez un texte :')
input_str = input()
input_phonem = get_phoneme(input_str)
res = check_string_array_match(input_phonem, insultes_phonemes_array)

# Affichage des %ages
for k,v in res.items():
    print(k, ' : ', v)