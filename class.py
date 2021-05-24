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
    def __init__(self, first, second):
        self.first = first
        self.second = second
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

print('*'*8)
# a = FourCal()
# b = FourCal()
# print(a)
# print(type(a))
# a.setdata(4,2)

# print(a.add())

a = FourCal(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.add())

#상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,2)
print(a.pow())

#메서드 오버라이딩: 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것. 
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first /self.second

a = SafeFourCal(4,0)
print(a.div())

#클래스 변수
class Family:
    lastname = "김"
print(Family.lastname) #김

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
Family.lastname = "박"
print(a.lastname)
print(b.lastname)
id(Family.lastname)
id(a.lastname)
id(b.lastname)
