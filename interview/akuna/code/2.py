
def closest_subtring(intList, n):
    min_index1 = 0
    min_index2 = 0
    min_dif = 10000000
    start_index = 0
    end_index = 0
    current_sum = intList[start_index]
    
    while (True):
        while (current_sum <= n):
            if (end_index < len(intList)-1):
                end_index += 1
                current_sum += intList[end_index]
            else:
                break
            
        sum1 = current_sum - intList[end_index]
        curr_dif = min([abs(sum1-n),abs(current_sum-n)])
        if (curr_dif<min_dif):
            if (abs(sum1-n)==curr_dif ):
                min_dif = abs(sum1-n)
                min_index1 = start_index
                min_index2 = end_index-1
            elif (abs(current_sum-n)==curr_dif ):
                min_dif = abs(current_sum-n)
                min_index1 = start_index
                min_index2 = end_index
                
        while (current_sum > n):
            start_index += 1
            current_sum -= intList[start_index]
            
        sum1 = current_sum - intList[start_index]
        curr_dif = min([abs(sum1-n),abs(current_sum-n)])
        if (curr_dif<min_dif):
            if (abs(sum1-n)==curr_dif ):
                min_dif = abs(sum1-n)
                min_index1 = start_index-1
                min_index2 = end_index
            elif (abs(current_sum-n)==curr_dif ):
                min_dif = abs(current_sum-n)
                min_index1 = start_index
                min_index2 = end_index
                
        if (end_index == len(intList)-1):
            break
            
    return (min_index1, min_index2)
        
        
    





intList = [3,4,5,6,7]
n = 5
print closest_subtring(intList, n)