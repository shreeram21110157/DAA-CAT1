import random
h1 = ''
h2 = ''
s1,s2 = '',''
l = ['A','C','G','T']
ls1 = random.choices(l,k = 16)
ls2 = random.choices(l,k = 16)
s1 = s1.join(ls1)
s2 = s2.join(ls2)
print(s1,s2)

fmat = []
for i in range(17):
    sub = []
    for j in range(17):
        sub.append(0)
    fmat.append(sub)

#print(fmat)

def max(k1,k2,k3):
    if(k1>k2):
        if(k1>k3):
            return k1
        elif(k2>k3):
            return k2
        else:
            return k3
    elif(k2>k3):
        return k2
    else:
        return k3
def check(w1,w2,i1,i2):
    if(i1<17 and i2<17):
        if(w1[i1] == w2[i2]):
            return 'c'
        else:
            return 'f'
    else:
        return'done'

def act(q1,q2,i1,i2):
    if(check(q1,q2,i1,i2)=='c'):
        fmat[i1+1,i2+1] = fmat[i1,i2] + 2
        global h1
        h1 = h1+q1[i1]
        act(q1,q2,i1+1,i2+1)
    elif(check(q1,q2,i1,i2)=='f'):
        fmat[i1+1,i2+1] = max(fmat[i1,i2],fmat[i1+1,i2],fmat[i1,i2+1]) - 1
        global h2
        h2 = h2+q2[i2]
        act(q1,q2,i1+1,i2+1)
    else:
        return
        
    




act(s1,s2,0,0)
print(fmat)
print(h1)
print(h2)