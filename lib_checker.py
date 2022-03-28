from gruut import sentences
from difflib import SequenceMatcher

"""--------------------------------
        Comparaisons de chaines
--------------------------------"""
# Comparaison de deux chaines de caractères
# Renvoie le %age de correspondance
def get_2strings_match_percent(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Comparaison d'une chaine de caractère avec une liste de chaines
# Renvoie un tableau associatif {element de la liste, pourcentage de correspondace}
def check_string_array_match(str,array):
    res = {}
    for insulte_phoneme in array:
        percent = get_2strings_match_percent(str, insulte_phoneme)
        if (percent >= 0.5):
            res[insulte_phoneme] = percent
    return res

"""--------------------------------
    Récupération des données
--------------------------------"""
# Récupération des mots dans le fichier 'insulte.txt'
def get_file_content(fic_url):
    result = open(fic_url, "r")
    all_lines= result.readlines()
    result.close()
    return all_lines

#Remplacement de tous les variants d'une lettre par celle-ci
def get_no_variants(all_lines, e_variants):
    list_line = []
    for line in all_lines:
        line_tmp = line.replace('\n', '') #Retrait du retour chariot
        #Boucle pour remplacer toutes les variantes de chaque lettre qui ont une pronociation proche
        for e_variant in e_variants:
            line_tmp = line.replace(e_variant, 'e')

        list_line.append(line_tmp)
    return(list_line)

"""--------------------------------
        Récupérations de phontiques
--------------------------------"""
# Retourne la phonetique d'un mot (ou phrase) donné
def get_phoneme(word):
    for sent in sentences(word, lang="fr"):
            res = ''
            for line_ph in sent:
                if line_ph.phonemes:
                    line_string = ''.join(line_ph.phonemes)
                    res = res + line_string
    return res

# Retourne une liste (en texte) des mots d'une liste, séparés par un retour chariot
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

def get_phonemes_array(data):
    result = []
    for line in data:
        for sent in sentences(line, lang="fr"):
            phrase = ''
            for line_ph in sent:
                if line_ph.phonemes:
                    line_string = ''.join(line_ph.phonemes)
                    phrase = phrase + line_string
        result.append(phrase)
    return result