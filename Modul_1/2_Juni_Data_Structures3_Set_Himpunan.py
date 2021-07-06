### Operasi himpunan pada SET
x={8,9,15,18,25,60}
y={9,25,60,85,83,75}

#### Union - Gabungan 2 SET atau lebih

z= x.union(y)
z1=y.union(x)

print(z1)
print(z)

### Irisan - Intersection

v=x.intersection(y)
###atau
#v=y.intersection(y)
print(v)

### Selisih - Difference
w = x.difference(y) ### sama seperti x-y
q = y.difference(x) ### sama seperti y-x

print(w)
print(q)

### Beda Setangkup - Symmetric Difference
t=x.symmetric_difference(y)
g=y.symmetric_difference(x)

print(t)
print(g)