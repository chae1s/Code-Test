"""
    피보나치 수를 배열 안에 집어넣는다.
    F(0) = 0, F(1) = 1
    F(2)는 F(0) + F(1)이므로 F(i) = fibo[i - 2] + fibo[i - 1]
    F(i)를 배열에 삽입
    i가 2에서 n이 될 때까지 반복하고
    반복이 끝나면 배열의 마지막 원소를 1234567로 나눈 나머지를 구한다.
"""

def solution(n):
    answer = 0
    fibo = [0, 1]
    i = 2
    while i <= n:
        fibo.append(fibo[i - 2] + fibo[i - 1])
        i += 1

    return fibo[-1] % 1234567
def main():

    print(solution(3))

    print(solution(5))





if __name__ == "__main__":
    main()