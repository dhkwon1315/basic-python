#계산기01
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

#계산기02
result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

#계산기가 많은 경우 클래스 사용
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(4))


#사칙연산 클래스 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        result =self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    
    
    

