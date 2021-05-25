a = int(input("A를 입력하세요")) #input은 조건이 끝나기 전까지 다음코드가 처리안됨
print(type(a))
b = int(input("B를 입력하세요"))
if (a % 2 == 0) and (b % 2 == 0): # 첫 번째 조건문
 print('두 수 모두 짝수입니다.')
if (a % 2 == 0) or (b % 2 == 0): # 두 번째 조건문 다음 실행문
 print('두 수 중 하나 이상이 짝수입니다.')