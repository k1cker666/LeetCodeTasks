import random
class InsertionSort:
    
    def __init__(self, NumberList: list):
        self.NumberList = NumberList
        
    def insertion_sort(self):
        for number in range(len(self.NumberList)):
            if number == 0:
                continue
            for item in self.NumberList:
                if self.NumberList[number] <= item:
                    self.NumberList.insert(self.NumberList.index(item), self.NumberList.pop(number))
                    break
        
        
NumberList = [random.randint(0, 50) for i in range(15)]

frst = InsertionSort(NumberList)
frst.insertion_sort()
print(frst.NumberList)