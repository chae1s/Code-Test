"""
    두 배열의 원소를 하나씩 가져와 곱한 합이 최소값이 되도록
"""
"""
    1. 두 배열의 원소를 곱한 값의 합이 최소값이 되려면 A 배열의 가장 작은 값 * B 배열의 가장 큰 값의 형태가 되어야 한다.
    2. A 배열은 오름차순으로 B 배열은 내림차순으로 정렬
    3. 같은 인덱스 번호의 숫자끼리 곱하고 answer에 더해준다.
"""

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for a, b in zip(A, B):
        answer += (a * b)

    return answer

def main():
    A1 = [1, 4, 2]
    B1 = [5, 4, 4]
    A2 = [1, 2]
    B2 = [3, 4]
    print(solution(A1, B1))
    print(solution(A2, B2))


if __name__ == "__main__":
    main()