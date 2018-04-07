import nltk
def get_sentence (json_text):
    outputs = json_text['outputs']
    data = outputs[0]['data']
    concepts = data['concepts']
    nouns = []
    other = []
    for elem in concepts[:5]:
        concept = elem['name']
        wordlist = concept.split()

        pos_tag = nltk.pos_tag(wordlist)
        for word in pos_tag:
            if pos_tag[word]=='NN':
                nouns.append(wordlist)
                break


    sentence = " a ".join(nouns[:-1])
    sentence = "There is a "+sentence+" and a "+nouns[-1]
    return sentence
