def saberi(a,b):
    return a+b
    # privremeno za analizu failed testova
    # return a-b
def oduzmi(a,b):
    return a-b
def pomnozi(a,b):
    return a*b
def podeli(a,b):
    if b==0:
        raise ValueError("Deljenje nulom nije dozvoljeno!")
    return a/b