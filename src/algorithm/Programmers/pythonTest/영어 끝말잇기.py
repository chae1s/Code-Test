
def solution(n, words):
    # 사람들이 말한 단어를 담을 list에 1번이 말한 단어를 삽입
    answer = [words[0]]
    # 몇 번째 사람이 말했는지를 담을 count, 다 성공했을 때를 대비해 -1을 대입
    count = -1
    # 끝말잇기가 되고 있는지 확인하기 위한 alphabet, 첫 단어의 마지막 글자를 대입
    alphabet = words[0][-1]
    # index 1번부터 반복문 시작
    for i in range(1, len(words)):
        # alphabet과 words[i]의 첫 단어가 일치하고 말한 단어 목록에 words[i]가 없으면
        if alphabet == words[i][0] and words[i] not in answer:
            # 단어 list에 words[i] 추가
            answer.append(words[i])
        # 첫 단어가 일치하지 않거나, 목록에 있을 경우
        else:
            # 단어의 index를 count에 넣기
            count = i
            break
        # 그 다음 단어의 첫 글자와 비교하기 위한 단어의 마지막 알파벳을 alphabet에 집어넣는다.
        alphabet = words[i][-1]

    # count가 -1가 아닐 때, 즉 탈락자가 생겼을 때 [탈락한 사람의 번호, 탈락한 회차]를 return,
    # 탈락자가 생기지 않았을 때 [0, 0]을 return 한다.
    return [count % n + 1, count // n + 1] if count != -1 else [0, 0]

def solution2(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i % n)+1, (i // n)+1]
    else:
        return [0, 0]


def main():
    n1 = 3
    words1 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    n2 = 5
    words2 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    n3 = 2
    words3 = ["hello", "one", "even", "never", "now", "world", "draw"]
    print(solution2(n1, words1))
    print(solution2(n2, words2))
    print(solution2(n3, words3))


if __name__ == "__main__":
    main()