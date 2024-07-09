############DEBUGGING#####################

# # Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()
# range(1, 20)은 1부터 19까지의 숫자를 생성하므로 20은 없다. 따라서 if i == 20:은 실행되지 않는다.
# range(1, 20) -> range(1, 21)

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
# randint(1, 6)은 1부터 6까지의 숫자를 생성하므로 dice_imgs의 index는 0부터 5까지이다. 따라서 dice_imgs[dice_num]은 index out of range error가 발생한다.
# randint(1, 6) -> randint(0, 5)

# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
# 1994를 입력하면 일치하는 조건이 없어서 아무것도 출력되지 않는다.
# year > 1994 -> year >= 1994

# # Fix the Errors
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
# input()의 리턴은 문자열이기 때문에 숫자로 변환해야 한다.
# print문이 들여쓰기가 되어 있지 않아서 에러가 발생한다.
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
# 대입이 필요한 곳에 == 이 사용되어 버그가 발생하였다.
# == -> =

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
# b_list.append(new_item)이 for문 밖에 있어서 for문이 끝나고 마지막 값만 추가된다.
# b_list.append(new_item)을 들여쓰기 한다.
