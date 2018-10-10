##problème22
def numero_lettre(lettre):
    liste_lettre=['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for x in range(len(liste_lettre)):
        if liste_lettre[x]==lettre:
            return x
print(numero_lettre('V'))

def solve22():
    f=open('p022_names.txt','r')
    liste=[]
    for ligne in f:
        liste+=ligne.split(',')
    liste=sorted(liste)
    score=0
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            score+=i*(int(numero_lettre(liste[j])))
    return score

print ('solve22=',solve22())
