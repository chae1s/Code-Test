"""
    핸드폰 자판은 하나의 키에 여러 개의 문자가 할당될 수 있다.
    핸드폰 자판을 이용해 특정 문자열을 작성할 때, 키를 최소 몇 번 눌러야 작성할 수 있는가?
"""
from string import ascii_uppercase
def solution(keymap, targets):
    answer = []
    a_to_z = sorted(ascii_uppercase)
    alphabet = {}
    for s in a_to_z:
        alphabet[s] = 101

    for str in keymap:
        for i in range(len(str)):
            if alphabet[str[i]] > (i + 1):
                alphabet[str[i]] = i + 1


    for target in targets:
        count = 0
        for i in range(len(target)):
            if alphabet[target[i]] == 101:
                count = -1
                break
            else:
                count += alphabet[target[i]]

        answer.append(count)

    return answer

def main():
    keymap1 = ["ABACD", "BCEFD"]
    target1 = ["ABCD","AABB"]
    keymap2 = ["AA"]
    target2 = ["B"]
    keymap3 = ["AGZ", "BSSS"]
    target3 = ["ASA","BGZ"]
    keymap4 = ["ABCE"]
    target4 = ["ABDE"]
    # print(solution(keymap1, target1))
    # print(solution(keymap2, target2))
    # print(solution(keymap3, target3))
    print(solution(keymap4, target4))


if __name__ == "__main__":
    main()