import time
import math
import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = len(arr)-1
        left = 0
        right = len(arr)-2
        if left != right:
            while(left < right):
                while(arr[left] < arr[pivot] and  left < len(arr)):
                    left += 1
                while(arr[right] > arr[pivot] and right > 0):
                    right -= 1
                if(left >= right):
                    pivotTemp = arr[pivot]
                    arr[pivot] = arr[left]
                    arr[left] = pivotTemp
                    break
                elif arr[pivot] == arr[left] and arr[pivot] == arr[right]:
                    left += 1
                else:
                    leftTemp = arr[left]
                    arr[left] = arr[right]
                    arr[right] = leftTemp
        else:
            if arr[pivot] < arr[left]:
                pivotTemp = arr[pivot]
                arr[pivot] = arr[left]
                arr[left] = pivotTemp
        return quicksort(arr[0:left])+[arr[left]]+quicksort(arr[left+1:len(arr)])

##List Generator methods

def randomNumGen(min, max):
    return math.floor(random.random()*(max - min + 1) + min)

def generateRandomList(size, min, max):
    arr = []
    for i in range(0,size):
        arr.append(randomNumGen(min,max))
    return arr

##Alternative and a little faster version

def quickSort(arr):
   sorter(arr,0,len(arr)-1)

def sorter(arr,first,last):
   if first<last:
       pivot = partition(arr,first,last)
       sorter(arr,first,pivot-1)
       sorter(arr,pivot+1,last)

def partition(arr,first,last):
   pivotvalue = arr[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
           leftmark += 1

       while rightmark >= leftmark and arr[rightmark] >= pivotvalue:
           rightmark -= 1

       if rightmark < leftmark:
           done = True
       else:
           temp = arr[leftmark]
           arr[leftmark] = arr[rightmark]
           arr[rightmark] = temp
           
   temp = arr[first]
   arr[first] = arr[rightmark]
   arr[rightmark] = temp
   return rightmark

##Alternative


testArray = generateRandomList(1000000,0,10000)
startTime = time.time()
quickSort(testArray)
print("The time it took is: " + str(time.time()-startTime) + "seconds")
