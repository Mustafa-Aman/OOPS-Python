# def raise_number(numb_do,numb_so):
#     result=1
#     for index in range(numb_so):
#         result=result*numb_do
#     return result
# print(raise_number(5,4))

# # TWO D LIST
# number_grid=[
#     [1,2,4,4],
#     [3,4,8,9],
#     [5,7,9,0],
#     [0]
# ]

# for saw in number_grid:
#     for dass in saw: 
#         print(dass)

# def translate(phrase):
#     tranlation=""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             if letter.isupper():
#                  tranlation=tranlation + "G" 
#             else:
#                  tranlation=tranlation + "g"
#         else:
#             tranlation=tranlation + letter
#     return tranlation

# print(translate (input("Enter a word: ")))

# try:
#     number= int(input("Enter a number: "))
#     answer=10/0
# except ValueError:
#     print("invalid input")
# except ZeroDivisionError as err :
#     print(err)

# employe_files=open("employes.txt", "a")

# employe_files.write("joffrey - sales man")

# employe_files.close()    

# import collections
      
# def bfs(graph,root):
#     visited=set()
#     queue= collections.deque([root])
    
#     while queue:
#         vertex=queue.popleft()
#         visited.add(vertex)
#         for i in graph[vertex]:
#             if i not in visited:
#                 queue.append(i)
#     print(visited)

# if __name__=="__main__":
#     graph={0:[1,2,3],1:[0,2],2:[0,1,4],3:[0],4:[2]}
#     bfs=(graph,0)


# def factorial(x):
#     if x ==1:
#         return
#     else:
#         return (x+factorial(x-1))
# numb=3

# print("The facotrial of", numb , "is", factorial(numb))

# # search alogorithm
# # linner way
# def binary_code(arr,x,n):
#     for i in range(0,n):
#         if (arr[i]==x):
#             return i
#     return -1
# arr=[22,23,55,6,30]
# x= 30
# n=len(arr)
# result=binary_code(arr,x,n)
# if(result == -1):
#     print("Element isnt present in the array")
# else:
#     print("Element is present at index",result)

# def binarycount(array,low,x,high):
#     while low<=high:
#         mid=low+high//2

#     if array[mid]==x:
#         return mid

#     elif array[mid]<=x:
#         low=mid + 1

#     elif array[mid]>=x:
#         high=mid - 1

# array=[1,2,3,4,5,6,7]
# x=1
# result=(binarycount(array,x,0,len(array)-1))

# if result !=-1:
#     print("Element is on index number ," +str(result))
# else:
#     print("Not found")

# print(result)


# Binary Search in python


def binarySearch(array, x, low, high):    
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:  
            low = mid + 1

        else:
            high = mid - 1

    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


# def partition(start, end, array):
#     pivot_index = start
#     pivot = array[pivot_index]
   
#     while start < end:
         
   
#         while start < len(array) and array[start] <= pivot:
#             start += 1
             
        
#         while array[end] > pivot:
#             end -= 1
         
        
#         if(start < end):
#             array[start], array[end] = array[end], array[start]
  
#     array[end], array[pivot_index] = array[pivot_index], array[end]
  
#     return end  
# def quick_sort(start, end, array):
     
#     if (start < end):
      
#         p = partition(start, end, array)
         
      
#         quick_sort(start, p - 1, array)
#         quick_sort(p + 1, end, array)        
# array = [ 10, 7, 8, 9, 1, 5 ]
# quick_sort(0, len(array) - 1, array)
 
# print(f'Sorted array: {array}')

# def shellSort(arr):
#     size=len(arr)
#     gap= size // 2

#     while gap > 0:
#         for i in range(arr,size):
#             anchor = arr[i]
#             j= i
#             while j>=gap and arr[j-gap]> anchor:
#                 arr[j]=arr[j-gap]
#                 j -=gap
#             arr[j]= anchor
#             gap= gap // 2

# arr2 = [12, 34, 54, 2, 3]
# print("input array:",arr2)
 
# shellSort(arr2)
# print("sorted array",arr2)           
    
