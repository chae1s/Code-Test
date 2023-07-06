"""
    괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻
    문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return
"""
"""
    1. 괄호를 넣을 배열 생성
    2. '('를 만나면 배열에 집어넣고 ')'를 만나면 배열에서 꺼낸다.
    3. 배열이 비어있으면 올바른 괄호
"""
def solution(s):
    answer = True
    pare = 0
    for str in s:
        if str == '(':
            pare += 1
        else:
            pare -= 1

    return pare == 0

def main():
    s1 = "()()"
    s2 = "(())()"
    s3 = ")()("
    s4 = "())(()"
    print(solution(s1))
    print(solution(s2))
    print(solution(s3))
    print(solution(s4))

if __name__ == "__main__":
    main()