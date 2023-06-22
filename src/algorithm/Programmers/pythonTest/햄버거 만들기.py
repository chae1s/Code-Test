"""
    ingredient의 원소 1, 2, 3은 순서대로 빵, 야채, 고기
    햄버거는 1, 2, 3, 1 순서로 만들어져야 한다.
    만들 수 있는 햄버거의 수는?
"""
"""
    1. ingredient의 원소를 문자열로 변경
    2. 문자열 안에 '1231'이 있으면 answer에 1 더하고 문자열 안의 '1231'을 ''로 변경
    3. 2번을 문자열 안에서 '1231'이 없어질 때까지 반복
"""

"""
    1. ingredient의 원소를 burger 배열에 집어넣기
    2. burger 안의 원소 중에 [1, 2, 3, 1]이 존재한다면 버거 1개 완성 (answer += 1) 
    3. 버거를 만든 재료는 burger 배열 안에 없어야 하므로 배열 안에서 4개 pop
"""
def solution(ingredient):
    answer = 0
    burger = []

    for num in ingredient:
        burger.append(num)
        if burger[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4):
                burger.pop()

    return answer

def main():
    ingredient1 = [2, 1, 1, 2, 3, 1, 2, 3, 1]
    ingredient2 = [1, 3, 2, 1, 2, 1, 3, 1, 2]
    ingredient3 = [1, 3, 2, 3, 1]
    print(solution(ingredient1))
    print(solution(ingredient2))
    print(solution(ingredient3))


if __name__ == "__main__":
    main()