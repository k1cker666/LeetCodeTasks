class Solution:
    x = int()
    
    def __init__(self, x):
        self.x = x
        
    def isPalindrome(self): #runtime 68 ms memory 11.8 mb
        a = str(self.x)
        x = list(a)
        x.reverse()
        i = 0
        for elem in x:
            if elem == list(a)[i]:
                i += 1
                rtype = True
            else:
                rtype = False
                break
        return rtype
    
    def isPalindrome2(self): #runtime 54 ms memory 11.64 mb
        answer = list()
        a = self.x
        if a < 0:
            rtype = False
            return rtype
        elif 0<=a<10:
            rtype = True
            return rtype
        else:
            while a >= 1:
                if a >= 10:
                    b = a % 10
                    a //= 10
                    answer.append(str(b))
                else:
                    answer.append(str(a))
                    break
        answer = int("".join(answer))
        if answer == self.x:
            rtype = True
        else:
            rtype = False
        return rtype
        
frst = Solution(121)
print(frst.isPalindrome2())

scnd = Solution(-121)
print(scnd.isPalindrome2())

thrd = Solution(10)
print(thrd.isPalindrome2())
