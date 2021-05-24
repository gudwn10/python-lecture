from typing import Counter

a=1.0
A=1.1
radius = 4.0
print('원의 반지름', A)
print('원의 반지름', a)
print('원의 면적', 3.14 * radius * radius)
print('원의 둘레', 2.0 * 3.14 * radius)

#리터럴/프로그래밍 언어에서 데이터 값을 나타냄
width = 10
height = 5
rectangle_area = width * height
print('사각형의 면적 :', rectangle_area) # 변수2개의 연산값을

name = "홍길동"
age = 2
print("안녕! 나는", name, "이야. 나는 나이가", age, "살이야.")
print("안녕! 나는 %s 이야. 나는 나이가 %d 살이야." %(name,age ))
print("안녕! 나는 {0} 이야. 나는 나이가 {1} 살이야.".format(name,age ))
print(f'안녕! 나는 {name} 이야. 나는 나이가 {age} 살이야')

my_age = 22
my_height = '177'
my_age = my_age + 1
my_height = my_height + 1
print(my_age, my_height)
