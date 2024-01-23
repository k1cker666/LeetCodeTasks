class TwoSum:
    nums = list()
    target = int()
    
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        
    def function(self):
        print(f"Набор чисел: {self.nums}")  # выводим исходный набор
        print(f"Ожидаемая сумма: {self.target}")  # выводим ожидаемый реузльтат
        answer = list()  # создаем список для сохранения ответов 
        for x in range(0, len(self.nums)):  # индекс первого слагаемого
            for y in range(0, len(self.nums)):  # индекс второго слагаемого
                if self.nums[x] + self.nums[y] == self.target:  # сравниеваем сумму
                    if x != y:
                        answer.append(x)  # сохраняем в список первый индекс
                        answer.append(y)  # сохраняем в список второй индекс 
        answer = set(answer)  # убираем повторения в списке 
        print(f"Индексы чисел: {answer}")
        
frst = TwoSum([2, 7, 11, 15], 9)
frst.function()