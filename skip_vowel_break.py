st='Programming'

#자음이 나타나는 동안만 출력하는 기능
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue #모음일 경우 반복문을 종료한다.
    print(ch)

print('The end')

