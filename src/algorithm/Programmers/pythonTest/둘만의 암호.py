"""
    문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔준다.
    index만큼의 뒤의 알파벳이 z를 넘어갈 경우 a로 돌아간다.
    skip은 제외하고 건너뛴다.

"""

"""
    알파벳 소문자를 넣을 dictionary 생성
    반복문을 이용하여 알파벳:번호 순으로 dictionary에 추가
    s에 있는 알파벳의 번호를 가져오고 그 번호에 index를 더하고 dictionary의 길이로 나눠준다.
    dictionary의 해당 번호를 가진 key값을 answer에 더해준다.
"""
def solution(s, skip, index):
    answer = ''
    alphabet = {}
    num = 0
    for i in range(26):
        if chr(i + 97) not in skip:
            alphabet[chr(i + 97)] = num
            num += 1

    for str in s:
        idx = (alphabet[str] + index) % len(alphabet)
        for key, value in alphabet.items():
            if value == idx:
                answer += key

    return answer

def main():
    s = 'aukks'
    skip = 'wbqd'
    index = 5
    print(solution(s, skip, index))


if __name__ == "__main__":
    main()