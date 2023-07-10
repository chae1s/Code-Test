
def solution(s):
    s_check = []
    for str in s:
        if len(s_check) == 0:
            s_check.append(str)
        else:
            if s_check[-1] == str:
                s_check.pop()
            else:
                s_check.append(str)
        print(s_check)

    return 1 if len(s_check) == 0 else 0


def solution_timeout(s):
    check = True
    while len(s) > 1 and check:
        s_list = list(s)
        for i in range(len(s_list) - 1):
            if s_list[i] == s_list[i+1]:
                del s_list[i:i+2]
                check = True
                break
            else:
                check = False

        s = ''.join(s_list)
    return 1 if len(s) == 0 else 0

def main():
    s1 = "baabaa"
    s2 = "cdcd"
    print(solution(s1))
    print(solution(s2))


if __name__ == "__main__":
    main()