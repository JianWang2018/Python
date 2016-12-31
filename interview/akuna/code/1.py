def binary_search(arr,target):
    low = 0
    high = len(arr)
    while (low != high):
        mid = (low+high)/2
        if (arr[mid] == target):
            low = mid
            break
        if (arr[mid] > target):
            low = mid + 1
        else:
            high = mid
    return low
        
    
    


def  subarray_median(arr, k):
     index = binary_search(arr,k)
     print index
     if (index % 2 == 0):
         return arr[index/2]
     else:
         return (arr[(index+1)/2] + arr[(index-1)/2])/2.0





arr = [4,4,4,4,4,3,2,1]
target = 1
print subarray_median(arr, target)