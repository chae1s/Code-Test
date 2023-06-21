"""
    달리기 경주
    선수들이 바로 앞 선수를 추월할 때마다 해설진들이 추월한 선수의 이름을 부름
    A, B, C 선수들이 순서대로 달리고 있을 때 B의 이름이 불렸다면 B, A, C 순서가 됨
    경주가 끝났을 때 1등부터 꼴등까지 return
"""

"""
    1. callings에서 불린 선수의 자리 파악
    2. 앞에서 달리고 있는 선수와 자리 변경
"""
def wrong_solution(players, callings):
    for calling in callings:
        idx = players.index(calling)
        temp = players[idx - 1]
        players[idx - 1], players[idx] = players[idx], players[idx - 1]

    return players

# ->  시간 초과 index는 배열 처음부터 calling이 나올때까지 탐색


"""
	1. 해설진에게 불리기 전 선수들의 등수를 dictionary에 선언 {선수 이름: index}
	2. 불린 선수의 index를 꺼내 앞 선수가 누군지 파악
	3. 배열 안에서 앞 선수와 불린 선수의 위치 변경
	4. dictionary 안에서도 앞 선수와 불린 선수의 등수 변경
"""

def solution(players, callings):
    rank = {player: i + 1 for i, player in enumerate(players)}
    players.index()
    for calling in callings:
        idx = rank[calling]
        prev_player = players[idx - 2]
        players[idx - 2], players[idx - 1] = players[idx - 1], players[idx - 2]
        rank[prev_player] += 1
        rank[calling] -= 1

    return players


if __name__ == "__main__":
    players = ["mumu", "soe", "poe", "kai", "mine"]
    callings = ["kai", "kai", "mine", "mine"]
    print(solution(players, callings))