n=int(input('Dati numarul de elemente din vector='))
z=[]
if n<10:
    print('Introduceti ',n,' elemente pentru vectorul creat')
    for i in range(0,n):
        x=int(input('Dati elementul='))
        z.extend([x])
    print(z)

    print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
    a=z
    print(a[::5])
    print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;', z[::-1])
    print('c)  sortează componentele tabloului în ordine descrescătoare;')
    c=sorted(z)
    c.sort(reverse=True)
    print(c)
    print('d)  afişează pe ecran doar componentele pare;')
    d=[]
    for i in range(0,len(z)):
        if z[i]%2==0:
            y=z[i]
            d.extend([y])
    print(d)
    print('e)  afişează pe ecran media aritmetică a componentelor pare;')
    e=[]
    for i in range(0,len(z)):
        if z[i]%2==0:
            y=z[i]
            e.extend([y])
    print(sum(e) / len(e))
    print('f)  afişează pe ecran doar componentele impare;')
    f=[]
    for i in range(0,len(z)):
        if z[i]%2!=0:
            y=z[i]
            f.extend([y])
    print(f)
    print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
    g=[]
    x=int(input("Dati x="))
    y=int(input("Dati y="))
    for i in range(0,len(z)):
        if (z[i] > x) and (z[i] % y !=0):
            t=z[i]
            g.extend([t])
    print(g)
    print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
    h=[]
    x=int(input("Dati x="))
    y=int(input("Dati y="))
    for i in range(0,len(z)):
        if (z[i] > x) and (z[i] < y ):
            t1=z[i]
            h.extend([t1])
    print(h)
    print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
    q=[]
    w=z
    for element in w:
        if (element<0) and (element%2!=0):
            element=w.index(element)
            q.extend([element])
    print(q)
    print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
    for i in range(0,len(w)):
        if (w[i] >9 and w[i]<100) or (w[i]>-100 and w[i] <-9):
            print(i)
    
    #k
    z1=z.copy()
    z1[0]=min(z1)
    print(f"k) înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv: {z1}")
    #l
    z2=z.copy()
    minimum=z2.index(min(z2))
    prima=z2[0]
    del(z2[minimum])
    z2.insert(minimum,prima)
    print(f'l) înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia este: {z2}')
    
    print(f'm)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură este:{e}')
    print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
    z3=[]
    for element in z:
        if element%3==0:
            z3.append(element)
    print(f"Tabloul care cuprinde doar elementele divizibile la 3 din cel initial este {z3}")
    #o
    z4 = []
    for i in z:
        divizori = []
        for j in range (1, i + 1):
            if i % j == 0:
                divizori.append(j)
        for j in range (i - 1, 0):
            if i % j == 0:
                divizori.append(j)
                if j < 0:
                    divizori.append(-j)
        print(divizori)
        if 1 <= len(divizori) <= 4:
            z4.append(i)
    print(f'o) creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori {z4}')
else:
    print("Dati un numar mai mic ca 10")