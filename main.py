
# ///////////////////
# <<< tuple >>>
# ///////////////////

t=(1,2,3,4,5)

print(type(t))

print(t)

for q in t:
    print(q)

# t::>>> add,del,delete,append {Error}

t2=()
print(t2)

n1=1
n2=4
n3=8
n4=0
n5=6

t=(n1,n2,n3,n4,n5)

print(t)

print(t[-1])

# /////////////////////
# <<<  dict >>>
# //////////////////////

d={'q':1,'w':2,'e':3}

print(type(d))

print(d)

kd=d.keys()
print(kd)

vd=d.values()
print(vd)

for x in d.keys():
    print(d[x])


d['a']=4
print(d)

# d.clear()
# print(d)

# del d 
# print(d)
# # NameError: name 'd' is not defined. Did you mean: 'id'?

# /////////////////
# <<< list >>>
# //////////////////

l=[-1,1,2,3,4]

print(l)

print(l[1]) 

l.append(4)
print(l)

l.insert(1,0)
print(l)

l.pop()
print(l)

l.remove(-1)
print(l)

# /////////////

l2=[['name',['ali','amir','ahmad']],['family',['alizade','amiry','ahmady']]]

print(l2)

print(l2[0])
print(l2[0][0])
print(l2[0][-1][-1],'\n')

print(l2[-1])
print(l2[-1][0])
print(l2[-1][-1])
print(l2[-1][-1][-1],'\n')

print('\n',l2[0][0],' :',l2[0][-1][-1])
print(l2[-1][0],' :',l2[-1][-1][-1])