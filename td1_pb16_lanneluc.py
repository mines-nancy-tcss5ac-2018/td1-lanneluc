##problème16
def solve16(n):
    a=2**n
    b=str(a)
    somme=0
    for k in range(len(b)):
        somme+=int(b[k])
    return somme
assert solve16(15)==26
print ('solve16(1000)=',solve16(1000))
