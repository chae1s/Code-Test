"""
    n은 1,000,000 이하의 자연수이므로 n보다 큰 숫자를 가져와 n과 비교
    숫자 n를 2진수로 바꾸고 '1'의 개수를 센다.
    반복문에서 가져온 숫자 또한 2진수로 바꾼 후 '1'의 개수를 센다.
    n의 '1' 개수와 반복문의 숫자 '1'의 개수가 같으면 그 수를 answer에 대입 후 반복문 종료
"""
def solution(n):
    answer = 0
    binary_n = format(n, 'b').count('1')
    for i in range(n + 1, 1000000):
        binary_i = format(i, 'b').count('1')
        if binary_n == binary_i:
            answer = i
            break

    return answer
def main():
    print(solution(78))

    print(solution(15))





if __name__ == "__main__":
    main()