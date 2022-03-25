from gruut import sentences

# text = "nyke ta mere"
text = "Hopital"
# text = "ordinateur"


for sent in sentences(text, lang="fr"):
    for word in sent:
        if word.phonemes:
            print(*word.phonemes)