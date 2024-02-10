import random

sorted_array = []
    
def split_array(array: list):
    left_half = list()
    right_half = list()
    mid_index = int(len(array)/2)
    for i in range(0, mid_index):
        left_half.append(array[i])
    for i in range(mid_index, len(array)):
        right_half.append(array[i])
    if len(left_half) > 1:
        split_array(left_half)
    elif len(left_half) == 1:
        sort_array(array=left_half)
    if len(right_half) > 1:
        split_array(right_half)
    elif len(right_half) == 1:
        sort_array(array=right_half)
    
 
def sort_array(array: list):
    global sorted_array
    if len(sorted_array) == 0:
        sorted_array.append(array[0])
    else:
        for item in sorted_array:
            if array[0] <= item:
                sorted_array.insert(sorted_array.index(item), array[0])
                break
            else:
                continue
        if array[0] > sorted_array[-1]:
            sorted_array.append(array[0])
        
NumberList = [random.randint(0, 50) for i in range(10)]

print(NumberList)
split_array(NumberList)
print(sorted_array)