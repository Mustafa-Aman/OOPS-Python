
# Same as {"a", "b","c"}
normal_set = set(["a", "b","c"])
 
print("Normal Set")
normal_set.add("N")
print(normal_set)

# A frozen set
frozen_set = frozenset(["e", "f", "g"])
 
print("\nFrozen Set")
# frozen_set.add("R")
print(frozen_set)

tuple=("h","d")
# tuple.add("F")
print(tuple)

# Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)
 
# accessing a element using key
print("Accessing a element using key:")
print(Dict['Name'])
 
# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(1))
 
# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]} 
print(myDict)

# Python program to demonstrate
# indexing in numpy array
import numpy as np
 
# Initial Array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)
 
# Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:2, ::2]
print ("Array with first 2 rows and"
    " alternate columns(0 and 2):\n", sliced_arr)
 
# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)

a = np.array([[1,2,3,4],[4,55,1,2],
              [8,3,20,19],[11,2,22,21]])
m = np.reshape(a,(4,4))
print(m)
 
# Accessing element
print("\nAccessing Elements")
print(a[1])
print(a[2][0])
 
# Adding Element
m = np.append(m,[[1, 15,13,11]],0)
print("\nAdding Element")
print(m)
 
# Deleting Element
m = np.delete(m,[1],0)
print("\nDeleting Element")
print(m)



stalk=[]

stalk.append("K")
stalk.append("f")
stalk.append("g")

print(stalk)