class TwoSum:
    nums = list()
    target = int()
    
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        
    def function(self):
        print(f"Набор чисел: {self.nums}")
        print(f"Ожидаемая сумма: {self.target}")
        answer = list()
        for x in range(0, len(self.nums)):
            for y in range(0, len(self.nums)):
                if self.nums[x] + self.nums[y] == self.target:
                    answer.append(x)
                    answer.append(y)
        answer = set(answer)
        print(f"Индексы чисел: {answer}")
        
frst = TwoSum([3, 2, 7, 9], 10)
frst.function()