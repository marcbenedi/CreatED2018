def farenheit_to_celsius(val):
    res = (val-32.0)*5/9.0
    return res
def celsius_to_farenheit(val):
    res = (val*9/5)+32
    return res

def create_sentence(val):
    sentC = "The temperature is "+str(val)+" degrees Celsius "
    sentF = " or "+str(celsius_to_farenheit(val))+" degrees Farenheit"
    return (sentC+sentF)
    
