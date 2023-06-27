package algorithm.Programmers.javaTest;

import java.util.LinkedList;
import java.util.Queue;

public class 게임_맵_최단거리 {
    private int[] dx = new int[]{-1, 1, 0, 0};
    private int[] dy = new int[]{0, 0, -1, 1};
    private int n;
    private int m;
    public int solution(int[][] maze) {
        n = maze.length;
        m = maze[0].length;
        // BFS 로직을 활용하는데,
        // 다음에 접근할 수 있는 칸을 maze의 가로 세로 크기 이내의 인접한 칸을 기준으로 판단

        // int[]를 담는 Queue, {x, y, 여태까지의 이동거리}
        Queue<int[]> visitNext = new LinkedList<>();

        // 미로에서 이미 도달한 적 있는 칸 임을 나타내기 위한 visited 이차원 배열
        boolean[][] visited = new boolean[6][6];
        visitNext.offer(new int[]{0, 0, 1});
        int answer = -1;

        // BFS 시작
        // Queue가 비어있지 않는 동안에
        while (!visitNext.isEmpty()) {
            // 다음에 갈 곳을 Queue에서 꺼낸다.
            int[] next = visitNext.poll();
            int nowX = next[0];
            int nowY = next[1];
            int steps = next[2];

            if (nowX == n - 1 && nowY == m - 1) {
                answer = steps;
                break;
            }

            // 4개의 방향을 확인
            // 1. 미로의 범위를 벗어나진 않는지
            // top[0], top[1]이 -1 보다는 크고, 6보다는 작아야 한다.
            // 2. 미로에서 진행 가능한 칸인지(0 또는 3)
            // 3. 아직 방문한 적 없는지
            for (int i = 0; i < 4; i++) {
                int nextX = nowX + dx[i];
                int nextY = nowY + dy[i];
                if (checkBounds(nextX, nextY) && maze[nextX][nextY] == 1 && !visited[nextX][nextY]) {
                    visitNext.offer(new int[]{nextX, nextY, steps + 1});
                    visited[nextX][nextY] = true;
                }
            }
        }

        return answer;
    }

    private boolean checkBounds(int x, int y) {

        return -1 < x && x < n && -1 < y && y < m;
    }

    public static void main(String[] args) {
        // 2가 시작점, 3이 목적지
        int answer = new 게임_맵_최단거리().solution(new int[][]{
                {1, 0, 1, 1, 1},
                {1, 0, 1, 0, 1},
                {1, 0, 1, 1, 1},
                {1, 1, 1, 0, 1},
                {0, 0, 0, 0, 1}
        });

        System.out.println(answer);
    }
}
