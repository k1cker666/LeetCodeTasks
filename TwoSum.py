class TwoSum:
    nums = list()
    target = int()
    
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        
    def function(self):
        print(f"Набор чисел: {self.nums}")  # выводим исходный набор
        print(f"Ожидаемая сумма: {self.target}")  # выводим ожидаемый реузльтат
        rtype = list()  # создаем список для сохранения ответов 
        for x in range(0, len(self.nums)):  # индекс первого слагаемого
            for y in range(0, len(self.nums)):  # индекс второго слагаемого
                if x == y:
                    continue
                if self.nums[x] + self.nums[y] == self.target:  # сравниеваем сумму
                    rtype.append(x)  # сохраняем в список первый индекс
                    rtype.append(y)  # сохраняем в список второй индекс 
        rtype = set(rtype)  # убираем повторения в списке 
        print(f"Индексы чисел: {rtype}")
        
    def function_version2(self):
        print(f"Набор чисел: {self.nums}")
        print(f"Ожидаемая сумма: {self.target}")
        rtype = list()
        for x in range(0, len(self.nums)):
            if (self.target - self.nums[x]) in self.nums: 
                y = self.nums.index(self.target - self.nums[x])
                if x != y:
                    rtype.append(x)
                    rtype.append(y)
        rtype = set(rtype)
        print(rtype) 
        
frst = TwoSum([3, 3], 6)
frst.function_version2()

scnd = TwoSum([2, 7, 11, 15], 9)
scnd.function_version2()

thrd = TwoSum([3, 2, 4], 6)
thrd.function_version2()