lst = []
a = [1,0,0,1]
b = [1,1,1,1]
c = [1,0,1,0 ]

lst.append(a)
lst.append(b)
lst.append(c)


from pprint import pprint

n = 2
gugudan = []
for n in range(10):
    ndan = []
    n = 2
    for i in range(1, 10):
        ndan.append( n * i )
    gugudan.append(ndan)

pprint(gugudan)



