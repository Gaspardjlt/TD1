# exercice 2
def longestword(draw) : 
    f=open('frenchssaccent.dic,'r')
    possible_words=[]
    for ligne in f:
        possible_words.append(ligne[0:len(ligne)-1])
    f.close()
    matching_words=[]
    for i in range (len(possible_words)):
        potentiel = possible_words[i]
        draw2 = draw[:]
        n = len(draw2)
        k = len(potentiel)
        for j in range (len(potentiel)):
            if potentiel[j] in draw2 :
                draw2.remove(potentiel[j])
        if len(draw2)==n-k:
        matching_words.append(potentiel)
    res = 0;
    index = -1;
    for k in range (len(matching_words)):
    if len(matching_words[k])>res:
        res = len(matching_words[k])
        indice = k

#exercice 3
points = {'a': 1, 'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'d':2,'g':2,'m':2,'b':3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10}
    
def score(u):
    res = 0
    for i in range (len(u)):
       res = res + points[u[i]]
    return res

def max_score(l):
    res = 0;
    indice = -1;
    for k in range (len(l)):
        if score(l[k])>res:
            res = score(l[k])
            indice = k
    return (res,l[k])

print(max_score(mots_possibles))

#exercice 4
def longestword_1joker(draw) : 
    f=open('frenchssaccent.dic,'r')
    possible_words=[]
    for ligne in f:
        possible_words.append(ligne[0:len(ligne)-1])
    f.close()
    matching_words=[]
    for i in range (len(possible_words)):
        potentiel = possible_words[i]
        draw2 = draw[:]
        n = len(draw2)
        k = len(potentiel)
        for j in range (len(potentiel)):
            if potentiel[j] in draw2 :
                draw2.remove(potentiel[j])
        if len(draw2)==n-k or len(tir2)==n-k+1:
        matching_words.append(potentiel)
    res = 0;
    index = -1;
    for k in range (len(matching_words)):
    if len(matching_words[k])>res:
        res = len(matching_words[k])
        indice = k

def score2(u):
    res = 0
    for i in range (len(u)):
        #on vérifie si la lettre n'est pas remplacée par un joker 
        if u[i] in tirage:
            res = res + points[u[i]]
    return res

def max_score2(l):
    res = 0;
    indice = -1;
    for k in range (len(l)):
        if score(l[k])>res:
            res = score(l[k])
            indice = k
    return (res,l[indice])

print(max_score2(mots_possibles2))