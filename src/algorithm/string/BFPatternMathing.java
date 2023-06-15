package algorithm.string;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BFPatternMathing {
    public void solution() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String target = reader.readLine();
        String pattern = reader.readLine();

        int tarIdx = 0;
        int patIdx = 0;

        // TODO tarIdx 전체 길이보다 작을 동안 반복한다.
        // TODO 존재하는지만 검색하면 된다 했을 경우 patIdx가 pattern.length()보다 작을 동안 반복한다.
        while (tarIdx < target.length() && patIdx < pattern.length()) {
            // TODO target[tarIdx]가 pattern[patIdx]랑 다를 경우
            if (target.charAt(tarIdx) != pattern.charAt(patIdx)) {
                // TODO targetIdx를 여태까지 이동한만큼 되돌린다.
                tarIdx -= patIdx;
                // TODO patIdx를 -1로 할당한다.
                patIdx = -1;
            }
            // TODO 다음 칸으로 이동한다.
            tarIdx++;
            patIdx++;

        }

        // TODO patIdx == pattern.length() 이면 성공이다. 어디에서 찾았는지 출력한다.
        if (patIdx == pattern.length()) System.out.println(tarIdx - patIdx);
        else System.out.println("404 Not Found");
    }

    public static void main(String[] args) throws IOException {
        new BFPatternMathing().solution();
    }
}
