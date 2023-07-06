"""
    s에서 0을 뺀 문자열의 길이를 이진 변환한다.
    이진변환한 수에서 다시 0을 뺀 문자열의 길이를 이진변환
    s가 '1'이 될 때까지 반복한 횟수와 제거된 0의 개수

"""
"""
    1. 이진 변환을 한 횟수를 구할 count, 제거한 0의 개수를 구할 zero 준비
    2. s가 '1'이 아닐 때까지 반복
    3. s가 '1'이 아니면 s 안의 0 개수를 세고 zero에 더해준다.
    4. s의 길이에서 0의 개수를 뺀 값을 이진 변환시켜주고 count 1 증가
    5. 배열에 count와 zero를 넣어서 return
"""
def solution(s):
    count = 0
    zero = 0
    while s != '1':
        num = s.count('0')
        zero += num
        s = format(len(s) - num, 'b')
        count += 1


    return [count, zero]




def main():
    s1 = "110010101001"
    s2 = "01110"
    s3 = "1111111"

    print(solution(s1))
    print(solution(s2))
    print(solution(s3))


if __name__ == "__main__":
    main()