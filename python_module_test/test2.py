# test2.py 파일
def sum_test(x, y):
	print(x + y, "이(가) 출력되었습니다")
	return x + y

# 직접 실행 되었을 때만 아래 코드 실행
if __name__ == "__main__":
    a = 1
    b = 2
    c = sum_test(a, b)

# 여기는 기본 실행 부분
a = 3
b = 4
c = sum_test(a, b)
