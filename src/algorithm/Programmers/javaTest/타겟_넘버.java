package algorithm.Programmers.javaTest;

public class 타겟_넘버 {
    public int solution(int[] numbers, int target) {
        dfs(numbers, 0, target, 0);
        return answer;
    }

    // 재귀함수 DFS를 할 예정이라, 정답을 클래스 단위로 관리
    private int answer = 0;

    // 재귀함수 DFS
    // numbers : 내가 사용할 숫자
    // next : 내가 다음에 사용할 차례의 숫자 -> 이번 DFS 호출에서 더하거나 뺄 숫자는 numbers[next]
    // target : 목표 값
    // sum : 이번 재귀까지 합한 값
    public void dfs(int[] numbers, int next, int target, int sum) {
        // 마지막 숫자를 쓴 시점에 next는 배열의 크기와 동일해진다.
        if (next == numbers.length) {
            // target과 일치하는지 확인
            if (sum == target) this.answer++;

        } else {
            // 더한 다음에 다음 숫자를 결정
            dfs(numbers, next + 1, target, sum + numbers[next]);
            // 뺀 다음에 다음 숫자를 결정
            dfs(numbers, next + 1, target, sum - numbers[next]);
        }
    }

    public static void main(String[] args) {
        int answer = new 타겟_넘버().solution(new int[]{1, 1, 1, 1, 1}, 3);
        System.out.println(answer);
    }
}
