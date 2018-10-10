def invers(chaine):
    chaine_inverse=''
    l=len(chaine)
    for i in range (1,l+1):
        chaine_inverse+=chaine[l-i]
    return chaine_inverse
    
def est_palindrome(chaine):
    chaine_inverse=invers(chaine)
    if chaine==chaine_inverse:
        return 1
    else:
        return 0
    
def add_reverse(chaine):
    chaine_inverse=invers(chaine)
    a=int(chaine)
    b=int(chaine_inverse)
    s=a+b
    chaine_somme=str(s)
    return chaine_somme
    
        
def est_nombre_de_Lychrel(n):
    chaine=str(n)
    nombre_palindrome=0
    compteur=1
    while est_palindrome(chaine)==0:
        chaine=add_reverse(chaine)
        compteur+=1
        if compteur>50:
            break
    if compteur<50:
        return 0
    else:
        return 1
            
def solve55(n):
    return sum(est_nombre_de_Lychrel(i) for i in range (n+1))

print (solve55(10000))

    
    