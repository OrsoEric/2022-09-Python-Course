#Dato il dizionario : 
foo = {"A" : 12, "Z" : 1, "H" : 23, "C" : 7}
#effettuare le print che restituiscano rispettivamente:
#{'A': 12, 'C': 7, 'H': 23, 'Z': 1}
#{'Z': 1, 'C': 7, 'A': 12, 'H': 23}

print(foo)
print( sorted( foo.items(), key=lambda my_lambda:(my_lambda[0], my_lambda[1]) ) )
print( sorted( foo.items(), key=lambda my_lambda:(my_lambda[1], my_lambda[1]) ) )