uma_lista= ['a', 'd', 'f']
uma_lista[1:1]= ['b', 'c']
print(uma_lista)
uma_lista[4:4]= ['e']
print(uma_lista)

a= [81,82,83]
a. append(5)
print(a)

b= [3,4,5,6]
b.reverse()
print (b)

b= [6,7,4,9,5,]
b.sort()
print(b)

a= [1,2,3,4,5,6]
print(a.index(4))

a= [1,2,3,4,8]
a.insert(2,100)
print(a)

#conta quantos tem de um determinado caráctere
a= [1,2,3,4,8]
print (a.count(4)) 
print(a)

#pop esclui 
a= [1,2,3,4,5]
a.pop(2)
print(a)
