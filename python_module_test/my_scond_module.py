import my_first_module

c = 5
d = 6

#sum_test가 my_first_module.py에 있으니 불러온다. 
#1. import를 하고 모듈에 있는 함수를 호출한다.
result = my_first_module.sum_test(c, d)

#2. from을 사용하여 모듈에 있는 함수를 호출한다
from my_first_module import sum_test
result = sum_test(c, d)