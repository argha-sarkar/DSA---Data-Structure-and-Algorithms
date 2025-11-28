
# Check if the given array is sorted in ascending order

arr = [10,20,3,0,40,50,60]
def isSort(arr):
    
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
           if arr[i] < arr[j]:
               return True
           else:
               return False
           
print(isSort(arr))
            