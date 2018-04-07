import nltk
def get_sentence (json_text):
    outputs = json_text['outputs']
    data = outputs[0]['data']
    concepts = data['concepts']
    nouns = []
    other = []
    negatives = []
    for elem in concepts[:5]:
        concept = elem['name']
        wordlist = concept.split()

        pos_tag = nltk.pos_tag(wordlist)
        for (word,tag) in pos_tag:
            if word=='no':
                negatives.append(concept.replace("no",""))
                break
            if tag=='NN':
                nouns.append(concept)
                break


    sentence = ""
    if len(nouns>0):
        if len(nouns==1):
            sentence = nouns[0]
        else:
            sentence = " a ".join(nouns[:-1])
        sentence = "There is a "+sentence
        if len (nouns>2):
            sentence = sentence +" and a "+nouns[-1]
    if len(negatives>0):
        if (len(negatives)==1):
            negSent = negatives[0]
        else:
            negSent = " nor a ".join(negatives)
        negSent = " However, there isn't any " + negSent
        sentence = sentence+negSent
    return sentence
