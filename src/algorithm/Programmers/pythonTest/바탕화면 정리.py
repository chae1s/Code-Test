"""
    바탕화면의 상태를 나타낸 문자열 배열 wallpaper
        빈칸 -> "." 파일이 있는 칸 -> "#"
    드래그하면 파일 선택

    최소한의 이동으로 모든 파일을 선택한다.
    드래그 시작점 S(lux, luy), 드래그 끝점 E(rdx, rdy)
    드래그한 거리 = |rdx - lux| + |rdy - luy|
"""

"""
    '#' 파일이 있는 인덱스 번호의 최대, 최소값을 알아야 함
    1. x 인덱스 배열, y 인덱스 배열 만든 후 최소값, 최대값 가져오기
    2. 맨 끝에 있는 파일까지 가져와야 하기 때문에 rdx, rdy는 max로 구한 값 + 1
"""

def solution(wallpaper):
    location_x = []
    location_y = []
    for i, str in enumerate(wallpaper):
        for j in range(len(str)):
            if str[j] == '#':
                location_x.append(i)
                location_y.append(j)

    answer = [min(location_x), min(location_y), max(location_x) + 1, max(location_y) + 1]
    return answer

def main():
    wallpaper1 = [".#...", "..#..", "...#."]
    wallpaper2 = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
    print(solution(wallpaper2))


if __name__ == "__main__":
    main()