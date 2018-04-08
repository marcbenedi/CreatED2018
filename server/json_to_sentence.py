import nltk
def startsWithVowel (word):
    vowels = 'aeiou'
    if word[0].lower() in vowels:
        return True
    else:
        return False
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
    if len(nouns)>0:
        if len(nouns)==1:
            sentence = nouns[0]
        else:
            sentence = " a ".join(nouns[:-1])
        sentence = "There is a "+sentence
        if len (nouns)>2:
            sentence = sentence +" and a "+nouns[-1]
    if len(negatives)>0:
        if (len(negatives)==1):
            negSent = negatives[0]
        else:
            negSent = " nor a ".join(negatives)
        negSent = " However, there isn't any " + negSent
        sentence = sentence+negSent

    sentence = indefiniteArticleFix(sentence)
    return sentence

def indefiniteArticleFix(sentence):
    s = sentence.split()
    for i in range(len(s)-1):
        if s[i]=="a" and startsWithVowel(s[i+1]):
            s[i]="an"

    return " ".join(s)
