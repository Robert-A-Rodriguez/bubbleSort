def bubbleSort(array):
    isSorted = False    #begin with an unsorted array
    while not isSorted:     #while the array is not sorted
        isSorted = True     #assume the array is sorted when we get to the top of the while loop
        for i in range(len(array)-1):  #loop through the array. we use -1 because we are comparing the current element with the next so when we get to the last element there is no next element
            if(array[i]>array[i+1]):    #if the current element is greater than the next one, swap those 2 elements
                swap(i, i+1, array)
                isSorted = False        #if we get to this point where we have to swap, it means that the array is not sorted
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


arr = [4,3,2,5,55,453,3003]
print(bubbleSort(arr))