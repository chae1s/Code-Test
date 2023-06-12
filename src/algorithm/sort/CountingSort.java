package algorithm.sort;

import java.util.Arrays;

public class CountingSort {
    public static void main(String[] args) {
        int[] arr = {0, 1, 4, 4, 3, 0, 5, 2, 5, 1};
        int n = arr.length;

        // 최대 최소는 구했다고 가정
        int max = 5;
        int min = 0;
        int k = max - min + 1;

        int[] counts = new int[k];
        for (int data : arr) {
            counts[data]++;
        }

        System.out.println(Arrays.toString(counts));

        // count 누적합
        for (int i = 0; i < k - 1; i++) {
            counts[i + 1] += counts[i];
        }
        System.out.println(Arrays.toString(counts));
        int[] output = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            // 현재 데이터를 인덱스로 counts 배열의 값 감소
            counts[arr[i]]--;
            // 그 곳이 현재 arr[i]의 마지막 index이다.
            int position = counts[arr[i]];
            output[position] = arr[i];

        }

        System.out.println(Arrays.toString(output));

    }
}