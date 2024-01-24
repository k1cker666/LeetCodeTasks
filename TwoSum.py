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
                if x == y:
                    continue
                if self.nums[x] + self.nums[y] == self.target:  # сравниеваем сумму
                    answer.append(x)  # сохраняем в список первый индекс
                    answer.append(y)  # сохраняем в список второй индекс 
        answer = set(answer)  # убираем повторения в списке 
        print(f"Индексы чисел: {answer}")
        
frst = TwoSum([3, 2, 4], 6)
frst.function()