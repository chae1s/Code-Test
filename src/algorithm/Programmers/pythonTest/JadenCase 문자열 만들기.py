"""
    모든 단어의 첫 문자가 대문자, 그 외의 알파벳은 소문자
"""
def solution(s):
    answer = s[0].upper()
    s = s.lower()
    for i in range(1, len(s)):
        if s[i - 1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i]
    return answer

def main():
    s1 = "3people unFollowed me"
    s2 = "for the last week"
    print(solution(s1))
    print(solution(s2))



if __name__ == "__main__":
    main()