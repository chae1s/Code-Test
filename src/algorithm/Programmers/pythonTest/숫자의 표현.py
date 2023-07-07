"""
    자연수 n을 연속된 자연수들로 표현하는 방법의 개수
    자연수 num, num+1, num+2, ... num+x의 합으로 표현
    만약 자연수 n이 연속된 3개의 자연수로 이루어져 있으면 n = 3 * num + 6 의 식을 계산해 num을 구할 수 있다.
    저 식의 6과 같은 숫자를 구하기 위해 num_list 배열에 0, 1, 3, 6, 10, 15, ... 처럼 0부터 i+1까지 더한 값을 넣어준다.
    그 더한 값은 n과 같거나 커서는 안된다.
    n에서 num_list의 원소를 뺀 값을 index + 1로 나눈 값이 0이 되면 num값이 구해진다.
    예를 들어 index = 2이고 num_list[2] = 3, n = 15일 때
    (15 - 3) % (2 + 1) 값은 0이고 (15 - 3) // (2 + 1) 값은 4이다.
    따라서 15는 4, 5, 6으로 만들 수 있다.
"""
def solution(n):
    answer = 0
    num = 0
    num_list = []
    for i in range(n):
        num += i
        if num >= n:
            break
        num_list.append(num)

    for i, value in enumerate(num_list):
        if (n - value) % (i + 1) == 0:
            answer += 1

    return answer

"""
    자연수 1부터 num까지 반복문을 돌린다.
    연속된 자연수를 더한 값이 sum
    이 sum값이 num과 같아지면 answer 1 증가 후 for j 반복문 종료
    sum값이 num보다 커지면 연속된 자연수의 합으로 num을 구할 수 없다는 의미, for j 반복문 종료

"""
def expressions(num):
    answer = 0
    for i in range(1, num + 1):
        sum = 0
        for j in range(i, num + 1):
            sum += j
            if sum == num:
                answer += 1
                break
            elif sum > num:
                break
    return answer
def main():
    n = 15
    print(solution(n))
    print(expressions(15))
    print(solution(20))
    print(expressions(20))




if __name__ == "__main__":
    main()