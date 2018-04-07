from espeak import espeak

def say(sentence):
    str_sentence  = str(sentence)
    symbols = "".join(str_sentence.split())
    if symbols.isalnum():
        espeak.synth(str_sentence)
        return True
    else:
        return False
