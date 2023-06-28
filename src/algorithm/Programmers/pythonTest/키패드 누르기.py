"""
    1, 4, 7 왼손 입력
    3, 6, 9 오른손 입력
    2, 5, 8, 0 가까운 손가락 입력, 왼손, 오른손 거리 같으면 왼손잡이인지, 오른손잡이인지 파악
    [[1, 2, 3]
     [4, 5, 6]
     [7, 8, 9]
     [*, 0, #]]
"""
def solution(number, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              0: [3, 1]}
    for num in number:
        if keypad[num][1] == 0:
            left = keypad[num]
            answer += 'L'
        elif keypad[num][1] == 2:
            right = keypad[num]
            answer += 'R'
        else:
            key = keypad[num]
            left_dis = abs(left[0] - key[0]) + abs(left[1] - key[1])
            right_dis = abs(right[0] - key[0]) + abs(right[1] - key[1])
            if left_dis < right_dis:
                left = key
                answer += 'L'
            elif left_dis > right_dis:
                right = key
                answer += 'R'
            else:
                if hand == 'left':
                    left = key
                    answer += 'L'
                else:
                    right = key
                    answer += 'R'
        print(left, right)

    return answer

def main():
    numbers1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand1 = 'right'
    numbers2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand2 = 'left'
    numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand3 = 'right'
    print(solution(numbers1, hand1))
    print(solution(numbers2, hand2))
    print(solution(numbers3, hand3))


if __name__ == "__main__":
    main()