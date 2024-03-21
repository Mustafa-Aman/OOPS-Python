import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))



a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
# print('number of dimensions :', arr.ndim)

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])



arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[1, 0, 2 ])

# This is from officalnumpy
arr_example = np.array([[1,2,3,4,5], [6,7,8,9,10]])

arr_example.shape

print('Last element from 2nd dim: ', arr_example[1, -1])



# This is from GEEKSFORGEEKS


# Python program to demonstrate
# array creation techniques
 
# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)
 
# Creating array from tuple
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)
 
# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)
 
# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s."
            "Array type is complex:\n", d)

# Slicing
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

temp = arr[:3, ::2]
print ("Array with first 2 rows and alternate"
                    "columns(0 and 2):\n", temp)




arr = np.array([1, 2, 3, 4, 5, 6, 7,])

print(arr[1:4:1])



arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])



arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])



arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])



arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[:2, 1:4])

# RESHAPING BY OFFICALNUMPY

a = np.arange(6)
print(a)

b=a.reshape(2,3)
print(b)
# newshape in reshaping
np.reshape(a, newshape=(1, 6), order='C')

a = np.array([1, 2, 3, 4, 5, 6])
a.shape
(6,)

a2 = a[np.newaxis, :]
a2.shape
(1, 6)

row_vector = a[np.newaxis, :]
row_vector.shape
(1, 6)

col_vector = a[:, np.newaxis]
col_vector.shape
(6, 1)

a = np.array([1, 2, 3, 4, 5, 6])
a.shape
(6,)

b = np.expand_dims(a, axis=1)
b.shape
(6, 1)

c = np.expand_dims(a, axis=0)
c.shape
(1, 6)



a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[a>=5])
b=a[a%2==0]
print(b)
# & and | operators
c = a[(a > 2) & (a < 11)]
print(c)


x = np.arange(1, 25).reshape(2,12)
x
np.hsplit(x,3)


# Python program to demonstrate
# basic operations on single array
 
a = np.array([1, 2, 5, 3])
 
# add 1 to every element
print ("Adding 1 to every element:", a+1)
 
# subtract 3 from each element
print ("Subtracting 3 from each element:", a-3)
 
# multiply each element by 10
print ("Multiplying each element by 10:", a*10)
 
# square each element
print ("Squaring each element:", a**2)
 
# modify existing array
a *= 2
print ("Doubled each element of original array:", a)
 
# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
 
print ("\nOriginal array:\n", a)
print ("Transpose of array:\n", a.T)

# .max,.min,.sum,.cumsum


a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b=a
b=np.arange(12)
print(b)

b=np.reshape(a,newshape=(-1,2), order='C')
print(b)

five_up = (a > 5) | (a == 5)
print(five_up)


# THIS FROM OFFICAL NUMPY
b = np.array([[3, 1], [2, 2]])
# b.sum(axis=1 or 0)


 
a = np.array([[1, 2],[3, 4]])
b = np.array([[4, 3],[1, 1]])

print ("Matrix multiplication:\n", a.dot(b))

# MENUPLEATING MATRIX FROM SLICING AND INDEX
data = np.array([[1, 2], [3, 4], [5, 6]])
data[0, 1]

data[1:3]

data[0:2, 0]

np.ones(3)

np.zeros(1)


arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)


arr = np.array([1, 2, 3, 4])

print(arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='U4')

print(arr)
print(arr.dtype)

# COPY AND VIEW


arr=np.array([1,2,3,4,5])
a=arr.copy()
arr[0]=25
print(arr)
print(a)

arr=np.array([1,2,3,4,5,6])
b=arr.view
arr[0]=56
print(arr)
print(b)



arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

data=np.array([[1,3],[4,5],[67,2]])
one_end=([[1]])
data+one_end


rng = np.random.default_rng()
rng.integers(5,size=(2,3))

import numpy as np

a=np.array([1,2,3,44,5,6,7,8,9,0,23,4,5,6,7,8,2,1,3,4,6,77,77])
unique_value=np.unique(a)
print(unique_value)
 
unique_values, indices_list = np.unique(a, return_index=True)
print(indices_list)


arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12],ndmin=5)

newarr=arr
newarr.reshape(2,3,2)
print(arr)
arr.shape


arr=np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8,9,10])

newarr = arr.reshape(2, 1, -1)

print(newarr)

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]]])
arr.reshape(-2)
import numpy as np
b = np.zeros(2,dtype=int)
print(b)  

import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)


import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

# FLATTEN AND RAVEL   
import numpy as np

x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a1=x.flatten()
a1[5]=60
print(x)
print(a1)

a2=x.ravel()
a2[0]=(23)
a2[4]=(45)
print(x)
print(a2)

# ITERATOR
import numpy as np

arr = np.array([1, 2, 3])

for idx,x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(idx,x)


import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)


import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)
import numpy as np

print(np.arange(1, 2,0.1))
import numpy as np

c = np.ones([5, 3],dtype=int)
print(c)
import numpy as np

x = np.linspace(0, 2, 10)
print(np.sin(x))


# import numpy
import numpy as np
  
# using numpy.core.fromrecords() method
gfg = np.core.records.fromrecords([(101, 'Jitender', 21),
                                    (102, 'Deepak', 20)], 
                            names = 'Rollno, Name, Age')
  
print(gfg.Age)
print(gfg.Name)

