import random
        
def quick_sort(numlist: list):
    plus_list = list()
    minus_lsit = list()
    if len(numlist) < 2:
        return numlist
    else:   
        middle_number = (min(numlist)+max(numlist))/2
        for item in numlist:
            if item <= middle_number:
                minus_lsit.append(item)
            elif item > middle_number:
                plus_list.append(item)
        return quick_sort(minus_lsit)+(quick_sort(plus_list))

           
NumberList = [random.randint(0, 50) for i in range(10)]

print(NumberList)
print(quick_sort(NumberList))

### работает,но иногда выдает ошибку RecursionError: maximum recursion depth exceeded in comparison
