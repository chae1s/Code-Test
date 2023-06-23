import re
"""
    1단계 대문자 -> 소문자
    2단계 알파벳 소문자, 숫자, '-', '_', '.' 만 사용 가능
    3단계 '.' 2번 이상 연속된 부분 -> '.'
    4단계 '.'가 처음이나 맨 끝에 나오면 제거
    5단계 빈 문자열이면 'a' 대입
    6단계 16자 이상이면 첫 15개의 문자 제외한 나머지 문자 제거 마지막 문자가 '.'이면 제거하기
    7단계 2자 이하라면 마지막 문자를 3글자가 될 때까지 반복
"""

def solution(new_id):
    answer = ''
    # 1단계 소문자로 변환
    answer = new_id.lower()
    # 2단계 알파벳 소문자, 숫자, -, _, . 가 아니면 ''로 변환
    answer = re.sub(r'[^a-z0-9-_.]', '', answer)
    # 3단계 .이 2개 이상 나올 경우 .으로 변경
    answer = re.sub(r'\.{2,}', '.', answer)
    # 4단계 첫 글자가 .일 때 맨 앞 문자 제거
    if answer.startswith('.'):
        answer = answer[1:]
    # 4단계 마지막 글자가 .일 때 맨 뒤 문자 제거
    if answer.endswith('.'):
        answer = answer[0:len(answer) - 1]
    # 5단계 answer의 길이가 0이면 a 대입
    if len(answer) == 0:
        answer = 'a'
    # 6단계 글자가 16 글자 이상일 때 앞에서부터 15번째 글자까지
    if len(answer) >= 16:
        answer = answer[0:15]
        # 마지막 문자가 .일 경우 마지막 문자 제거
        if answer[-1] == '.':
            answer = answer[0:len(answer) - 1]
    # 7단계 문자가 3글자가 되지 않는다면 3글자가 될 때까지 마지막 문자 더해주기
    if len(answer) <= 2:
        for i in range(len(answer), 3):
            answer += answer[-1]

    return answer

def main():
    new_id1 = '...!@BaT#*..y.abcdefghijklm'
    new_id2 = 'z-+.^.'
    new_id3 = '=.='
    new_id4 = '123_.def'
    new_id5 = 'abcdefghijklmn.p'
    print(solution(new_id1))
    print(solution(new_id2))
    print(solution(new_id3))
    print(solution(new_id4))
    print(solution(new_id5) == 'abcdefghijklmn')


if __name__ == "__main__":
    main()