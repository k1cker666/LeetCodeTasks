import random
class BubbleSort:
    
    def __init__(self, NumberList: list):
        self.NumberList = NumberList
        
    def bubble_sort(self):
        count = len(self.NumberList)
        while count != 1:
            for number in range(count):
                if number == count-1:
                    count -= 1
                elif self.NumberList[number] > self.NumberList[number+1]:
                    self.NumberList[number], self.NumberList[number+1] = self.NumberList[number+1], self.NumberList[number]
                       
NumberList = [random.randint(0, 50) for i in range(10)]

frst = BubbleSort(NumberList)
frst.bubble_sort()
print(frst.NumberList)