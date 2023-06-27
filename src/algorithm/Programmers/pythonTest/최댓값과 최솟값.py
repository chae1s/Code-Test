"""
    문자열 s에는 공백으로 구분된 숫자들 저장
    s에 나타나는 숫자 중 최소값과 최대값을 찾아 "최소값 최대값" 형태로 문자열 반환
"""

def solution(s):
    numList = []
    for num in s.split(' '):
        numList.append(int(num))

    answer = '{0} {1}'.format(min(numList), max(numList))

    return answer

def main():
    s1 = "1 2 3 4"
    s2 = "-1 -2 -3 -4"
    s3 = "-1 -1"
    print(solution(s1))
    print(solution(s2))
    print(solution(s3))

if __name__ == "__main__":
    main()