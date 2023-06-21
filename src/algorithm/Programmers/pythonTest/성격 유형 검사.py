"""
    성격 유형 검사지
    4개의 지표로 성격 유형 구분 -> RT / CF / JM / AN
    choices 1 ~ 7 -> 매우 비동의, ..., 매우 동의
    ex. AN
    choices: 1 -> A +3, 2 -> A +2, 3 -> A +1, ..., 6 -> N +2, 7 -> N+3
    만약 A의 점수와 N의 점수가 같으면 오름차순으로 선택 -> A
"""

"""
    1. dictionary에 성격유형: 0 을 집어넣기 -> 각 성격 유형의 점수를 0으로 맞추기
    2. choices의 점수가 4 미만이면 survey의 지표 중 앞에 있는 성격 유형의 점수 증가
       choices의 점수가 4 초과이면 survey의 지표 중 뒤에 있는 성격 유형의 점수 증가
    3. 만약 같은 지표의 두 성격 유형의 점수가 다르면 높은 점수를 가진 성격 유형이, 점수가 같으면 오름치순으로 선택하여 answer에 더하기  
"""

def solution(survey, choices):
    answer = ''
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i, str in enumerate(survey) :
        if choices[i] < 4:
            dic[str[0]] = dic[str[0]] + 4 - choices[i]
        elif choices[i] > 4:
            dic[str[1]] = dic[str[1]] + choices[i] - 4

    if dic['T'] > dic['R'] :
        answer += 'T'
    else:
        answer += 'R'
    if dic['F'] > dic['C'] :
        answer += 'F'
    else:
        answer += 'C'
    if dic['M'] > dic['J'] :
        answer += 'M'
    else:
        answer += 'J'
    if dic['N'] > dic['A']:
        answer += 'N'
    else:
        answer += 'A'

    return answer

def main():
    survey1 = ["AN", "CF", "MJ", "RT", "NA"]
    choices1 = [5, 3, 2, 7, 5]
    survey2 = ["TR", "RT", "TR"]
    choices2 = [7, 1, 3]

    print(solution(survey1, choices1))
    print(solution(survey2, choices2))


if __name__ == "__main__":
    main()